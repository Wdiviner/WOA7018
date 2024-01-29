#!/usr/bin/env python
import rospy
import subprocess
from std_msgs.msg import String
import os

# Initialize the ROS node
rospy.init_node('detection', anonymous=True)

# Create a publisher to publish detection results
pub = rospy.Publisher('/detect_result', String, queue_size=10)

global process

# Callback function to handle incoming messages
def message_callback(msg):
    rospy.loginfo("Received message: %s", msg.data)
    print('message' + str(msg.data))

    if str(msg.data)=='start':
        # Define the command to run YOLOv7 object detection
        command = "python3 yolov7/detect.py --weights best.pt --conf 0.1 --source 0"
        subprocess.run(command, shell=True)

        process = subprocess.run(command, shell=True)
        print("start")

    elif str(msg.data)=='stop':
        # Terminate the process
        process.terminate()
        print("stop")

# Continuously listen for messages and call the message_callback
while not rospy.is_shutdown():
    rospy.Subscriber('/sr_result', String, message_callback)
    rospy.spin()
