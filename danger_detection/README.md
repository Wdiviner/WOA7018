# Readme - Robot Danger Detection System

## Introduction
This readme provides instructions on how to run the Robot Danger Detection System on Ubuntu 20.04 LTS using ROS Noetic. The system utilizes speech recognition, object detection, and text-to-speech capabilities. It can be triggered using voice commands to wake up the robot, initiate object detection for dangerous items, send alerts to an email address in case of a threat detection, and terminate the program upon receiving a stop command.

## Prerequisites
Before running the Robot Danger Detection System with ROS Noetic on Ubuntu 20.04 LTS, ensure you have the following prerequisites installed:

- Ubuntu 20.04 LTS
- ROS Noetic (Robot Operating System)
- Python 3.x
- Required Python libraries (install using `pip` if not already installed):
  - [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
  - [OpenCV](https://pypi.org/project/opencv-python/)
  - [smtplib](https://docs.python.org/3/library/smtplib.html) (for email notification)
  - [email](https://docs.python.org/3/library/email.html) (for email notification)
  - [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/)

## Running the Robot Danger Detection System
Follow these steps to run the Robot Danger Detection System:

1. Open a terminal and navigate to the directory containing the project files.

2. Run the following commands to execute the individual components of the system:

   ```shell
   python3 speech_recognize.py
   ```

   - Use the "start" command to wake up the robot. It will wait for the "start" command to initiate further actions.

   ```shell
   python3 detect_danger.py
   ```

   - Once the robot is awake, this command will activate the object detection system to identify dangerous items.

   ```shell
   python3 tts.py
   ```

   - If a dangerous item is detected, the system will issue a warning and notify the specified email address (configured within the `tts.py` script).

3. To terminate the program, use the "stop" command in the speech_recognize.py terminal:

   ```shell
   stop
   ```

   - This will stop the program and conclude the execution.

## Configuration
- Email Notifications: To enable email notifications, open the `tts.py` file and update the email configuration parameters (SMTP server, sender email, recipient email, etc.) as per your requirements.

## Notes
- Ensure that your system's microphone is set up and functioning correctly for speech recognition to work.

## Disclaimer
This system is intended for educational and experimental purposes only. It is not a guaranteed safety device and should not be relied upon as such. Always exercise caution and use appropriate safety measures in potentially dangerous situations.
