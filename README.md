# **AI Fitness Tracker**  
_A project developed as part of the **AICTE Internship**_

---

## **About the Project**
The **AI Fitness Tracker** is an AI-powered workout assistant designed to help users track their workout repetitions accurately. Using computer vision techniques and real-time pose estimation, the app analyzes workout videos or live webcam feeds to provide feedback during exercise sessions. This project is the foundation for a full-fledged AI fitness trainer application, with plans to add advanced features and an improved user interface.

---

## **Features**
  - Automatically detects arm movements and counts bicep curl repetitions.
  - Works with both pre-recorded videos and live webcam streams.
  - Displays the count of left and right arm bicep curls live on the screen.
  - Visualizes key landmarks (shoulder, elbow, wrist) and angles during the workout.
  - Has user-friendly Streamlit interface for uploading videos or analyzing workouts via webcam.
  - Powered by the YOLOv8 pose model for precise keypoint detection.

---

## **Setup Instructions**

### 1. **Clone the Repository**
   Use the following commands to clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/<your-username>/AI_Fitness_Tracker-AICTE_Internship.git
   cd AI_Fitness_Tracker-AICTE_Internship
  ```
### 2. **Install Dependencies**
   Ensure you have Python installed (version 3.8+ recommended). Then, install the required libraries:
   ```bash
   pip install -r requirements.txt
  ```
### 3. Run the Application
  Launch the Streamlit app using the following command:
  ```bash
   streamlit run app.py
  ```

## **How to Use**
1. **Select Input**:
   - Choose between **Upload Video** or **Use Webcam** in the application interface.

2. **For Upload Video**:
   - Click on **Upload Video** and select a workout video (e.g., bicep curl video) for analysis.

3. **For Webcam**:
   - Click on the **Start Webcam** button to start real-time tracking.

4. **View Results**:
   - The app will display live feedback, including:
     - Left and right bicep curl counts.
     - Visual landmarks (shoulder, elbow, wrist) and connecting lines.

---

## **Technology Stack**
- **Python**: Core programming language for backend logic.
- **YOLOv8**: Pose estimation model for detecting keypoints with precision.
- **OpenCV**: Real-time video processing and visualization.
- **Streamlit**: Interactive web-based interface for seamless user interaction.
- **NumPy**: Mathematical computations for angle calculations.

---

## **Contact**
For questions or feedback, feel free to reach out via:
- **Email**: [your-email@example.com](mailto:deekshitha1325@gmail.com)
- **GitHub**: [your-github-username](https://github.com/deekshitha-3)


This project serves as the foundation for a comprehensive **AI Fitness Trainer Project**. 


