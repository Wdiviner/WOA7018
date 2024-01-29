#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from gtts import gTTS
import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

rospy.init_node('texttospeech', anonymous=False)

count = 0
item = ''
item_count = 0

def send_email(subject, message, to_email):
    from_email = "woa7018robot@gmail.com"
    password = "tduz mhyj qtwn tusd"

    # create email object
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # add email content
    msg.attach(MIMEText(message, 'plain'))

    # create SMTP server connect
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()  # enable TLS transport
    server.login(from_email, password)
    
    # send email
    server.send_message(msg)
    server.quit()

def message_callback(msg):
    rospy.loginfo("Received message: %s", msg.data)

    # if msg.data == 'a dangerous good is detected':
    if 'a dangerous good is detected' in msg.data:
        global count, item, item_count
        count += 1
        
        info = msg.data.split(",")

        if item != info[-1] :
            item = info[-1]
        
        if item == info[-1]:
            item_count += 1
        
        if item_count % 10 == 0 :
            info = msg.data.split(",")
            mytext = 'Dangerous'+ info[-1] +' are detected. Please be careful now.'
            language = 'en'
            myobj = gTTS(text=mytext, lang=language, slow=False)
            myobj.save("audio.mp3")
            os.system("mpg321 audio.mp3")
            
        if count % 10 == 0 :
            print("send warning email")
            send_email("Robot Warning", info[-1] + " has been detected, please be careful!", "zhiyuantian816@gmail.com")

def listener():
    rospy.Subscriber('/detect_result', String, message_callback)
    rospy.spin()

if __name__ == '__main__':
    listener()
