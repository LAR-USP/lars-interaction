# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String
import subprocess
import time


pub = rospy.Publisher('robot_face/text_out', String, queue_size=1) 


def split_sentences( data ):
    return data.split('.')


def callback(data):
    print( 'speak callback function' )
    if len(data.data) <=2 and (':' in data.data or data.data == '.'):
        pub.publish(data.data) 
        return 1

    text = data.data.strip('=')
    pub.publish( text )
    time.sleep(0.5)
    print( 'published sentece' )
    subprocess.call( [ 'lianetts', '-s',  '1.0', text ] ) # blocking
    print( 'sentence spoken!' )


def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('speak', String, callback) 
    #while not rospy.core.in_shutdown():
    #    rospy.rostime.wallsleep(0.5)
    rospy.spin()

listener()
