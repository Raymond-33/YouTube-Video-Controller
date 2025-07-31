Hand Gesture-Controlled YouTube Video Controller

Overview:
This project is a real-time computer vision system that allows users to control YouTube video playback using hand gestures. Built using Python and OpenCV, the system captures live hand gestures via webcam and maps them to specific actions such as play, pause, volume control, and next/previous navigation.

Key Features:
Real-time hand gesture detection using OpenCV
Gesture-based control for:
Play / Pause
Volume Up / Down
Skip Forward / Backward
Mute / Unmute

Uses landmarks detection for high accuracy
Compatible with major web browsers and YouTube interface

Technologies Used:
Python
OpenCV
MediaPipe (for hand landmark detection)
PyAutoGUI (to control keyboard and mouse events)
Time and Math libraries

Project Workflow:
Capture video input through webcam
Detect hand landmarks using MediaPipe
Map specific finger gestures to corresponding YouTube functions
Trigger system-level keystrokes (e.g., spacebar for play/pause) using PyAutoGUI
Provide on-screen feedback for detected gestures

Setup Instructions:
Ensure Python 3.x is installed
Install required libraries using pip:
pip install opencv-python mediapipe pyautogui
Run the main Python script:
python hand_gesture_youtube_control.py
Open YouTube in your browser and place the video in focus
Use hand gestures in front of the webcam to control the video

Project Output:
Achieved an accuracy of approximately 85% in detecting predefined hand gestures
Demonstrated smooth and responsive control in real-time

Limitations:
Requires good lighting conditions for optimal detection
Works best with one hand in the frame
May not work reliably in cluttered or low-contrast backgrounds

Applications:
Assistive technology for hands-free media control
Gesture-based interfaces for smart TVs and kiosks
Potential use in AR/VR and gaming environments
