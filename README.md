Face Tracking and Orientation Detection
This project tracks a user’s face in real-time using the webcam and monitors their face orientation to ensure they are facing the screen. The code uses OpenCV for image processing, Mediapipe for facial landmark detection, and NumPy for angle calculations. It’s designed to give feedback if the user looks away from the screen.

Features
Face Landmark Detection: Utilizes Mediapipe’s Face Mesh model to detect facial landmarks in real-time.
Face Orientation Calculation: Computes angles between selected face landmarks to determine face orientation.
Visual Feedback: Displays an alert if the user is not facing the screen.
User-Friendly Overlay: Provides a semi-transparent overlay for easy-to-read alerts.
Requirements
Python 3.x
OpenCV
Mediapipe
NumPy
Install dependencies using:

bash
Copy code
pip install opencv-python mediapipe numpy
Usage
Run the Script: To start face tracking, run:

bash
Copy code
python mono.py
Exit: Press 'q' to exit the webcam display window.

Code Overview
1. calculate_angle function
Calculates the angle between three facial landmarks to determine face orientation.

2. draw_text function
Displays a semi-transparent text box with an alert if the user is not looking at the screen.

3. monitor_face_position function
Captures real-time video, detects face landmarks, calculates orientation angles, and displays alerts when the face deviates from the screen.

How It Works
The code maps critical face landmarks (nose and eyes) and calculates the angles to assess face orientation. If the user’s face turns away from the screen by more than a threshold angle (35 degrees), an alert is shown. The system continues to monitor until manually exited.

Example

Future Enhancements
Multiple Face Detection: Support for monitoring multiple faces.
Extended Landmark Analysis: Use more landmarks for improved accuracy.
Custom Alert Sounds: Add audio feedback when the user looks away from the screen.
