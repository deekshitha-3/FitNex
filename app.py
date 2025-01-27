import streamlit as st
from ultralytics import YOLO
import cv2
import numpy as np

model = YOLO('yolov8n-pose.pt')

st.title("Bicep Curl Trainer")
st.write("Choose to either upload a workout video or use your webcam for live analysis!")

input_option = st.radio("Select Input Method:", ("Upload Video", "Use Webcam"))

class Angles:
    def __init__(self, p1, p2, p3):
        self.point_one = p1
        self.point_two = p2
        self.point_three = p3

    def unpackAngles(self):
        self.x, self.y, _ = self.point_one
        self.x1, self.y1, _ = self.point_two
        self.x2, self.y2, _ = self.point_three

    def findAngles(self):
        self.unpackAngles()
        v1 = np.array([self.x, self.y]) - np.array([self.x1, self.y1])
        v2 = np.array([self.x2, self.y2]) - np.array([self.x1, self.y1])
        angle_rad = np.arccos(
            np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        )
        angle_deg = np.degrees(angle_rad)
        return int(angle_deg)

    def drawPointCircles(self, frame):
        self.unpackAngles()
        cv2.circle(frame, (int(self.x), int(self.y)), 5, (0, 0, 255), -1)
        cv2.circle(frame, (int(self.x1), int(self.y1)), 5, (0, 0, 255), -1)
        cv2.circle(frame, (int(self.x2), int(self.y2)), 5, (0, 0, 255), -1)

    def drawAngleLine(self, frame):
        self.unpackAngles()
        color = (90, 200, 66)
        cv2.line(frame, (int(self.x), int(self.y)), (int(self.x1), int(self.y1)), color, 2)
        cv2.line(frame, (int(self.x1), int(self.y1)), (int(self.x2), int(self.y2)), color, 2)

def process_video(cap):
    # Initialize Counters
    counter_L = counter_R = 0
    direction_L = direction_R = 0
    frame_window = st.empty()  

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        original_height, original_width = frame.shape[:2]
        scale_factor_width = 600 / original_width
        scale_factor_height = 400 / original_height
        scale_factor = max(scale_factor_width, scale_factor_height)
        new_width = int(original_width * scale_factor)
        new_height = int(original_height * scale_factor)
        frame = cv2.resize(frame, (new_width, new_height))

        result = model(frame)
        try:
            keypoints = result[0].keypoints.data[0]

            right_wrist = keypoints[10]
            right_elbow = keypoints[8]
            right_shoulder = keypoints[6]
            if all(right_wrist) and all(right_elbow) and all(right_shoulder):
                right_angle = Angles(right_wrist, right_elbow, right_shoulder)
                rightHandAngle = right_angle.findAngles()
                right_angle.drawPointCircles(frame)
                right_angle.drawAngleLine(frame)
                if rightHandAngle <= 70:
                    if direction_R == 0:
                        counter_R += 0.5
                        direction_R = 1
                if rightHandAngle >= 100:
                    if direction_R == 1:
                        counter_R += 0.5
                        direction_R = 0

            left_wrist = keypoints[9]
            left_elbow = keypoints[7]
            left_shoulder = keypoints[5]
            if all(left_wrist) and all(left_elbow) and all(left_shoulder):
                left_angle = Angles(left_wrist, left_elbow, left_shoulder)
                leftHandAngle = left_angle.findAngles()
                left_angle.drawPointCircles(frame)
                left_angle.drawAngleLine(frame)
                if leftHandAngle <= 70:
                    if direction_L == 0:
                        counter_L += 0.5
                        direction_L = 1
                if leftHandAngle >= 100:
                    if direction_L == 1:
                        counter_L += 0.5
                        direction_L = 0

        except Exception as e:
            print(f"Error processing frame: {e}")
            pass

        cv2.putText(frame, f"Left Count: {int(counter_L)}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        cv2.putText(frame, f"Right Count: {int(counter_R)}", (20, 80),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_window.image(frame)

    cap.release()

if input_option == "Upload Video":
    video_file = st.file_uploader("Upload a Video", type=["mp4", "avi", "mov"])
    if video_file:
        cap = cv2.VideoCapture(video_file.name)
        process_video(cap)

elif input_option == "Use Webcam":
    if st.button("Start Webcam"):
        cap = cv2.VideoCapture(0)  # Open webcam
        process_video(cap)

st.write("Processing Complete!")