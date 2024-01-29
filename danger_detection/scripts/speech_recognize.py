#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import speech_recognition as sr

result = ''

rospy.init_node('googlesr', anonymous=False)
pub = rospy.Publisher('/sr_result', String, queue_size=10)

def googlesr():

    while not rospy.is_shutdown():
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        with sr.Microphone() as source:
            print(">>> Say something!")
            #audio = r.listen(source)
            audio = r.record(source, duration=5)
            
        # recognize speech using Google Speech Recognition
        try:
            result = r.recognize_google(audio)
            print("SR result: " + result)
            detect_start(result)
            detect_stop(result)
        except sr.UnknownValueError:
            print("SR could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))
        
def detect_start(result):
    substring = ['start', 'begin' 'launch']
    for i in range(len(substring)):
        if substring[i] in result:
            print("Start dangerous items detection!")
            pub.publish('start')

def detect_stop(result):
    substring = ['stop', 'finish']
    for i in range(len(substring)):
        if substring[i] in result:
            print("End dangerous items detection!")
            pub.publish('stop')


if __name__ == '__main__':
    try:
        googlesr()
    except rospy.ROSInterruptException:
        pass

