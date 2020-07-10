#!/usr/bin/env python

import rospy
from topic_tutorial_2.msg import Mymsgs

NAME_TOPIC = '/msgs_talk'
NAME_NODE = 'Sub_node'

def callback(msgs):

    rospy.loginfo(msgs.x + 2*msgs.y)

if __name__ =='__main__':
    
    rospy.init_node(NAME_NODE, anonymous=True)

    sub = rospy.Subscriber(NAME_TOPIC, Mymsgs, callback)

    rospy.spin()
