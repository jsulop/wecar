#!/usr/bin/env python

import rospy
from topic_tutorial_2.msg import Mymsgs

NAME_TOPIC = '/msgs_talk'
NAME_NODE = 'Pub_node'

if __name__ == '__main__':

    rospy.init_node(NAME_NODE, anonymous=True)

    pub = rospy.Publisher(NAME_TOPIC, Mymsgs, queue_size = 10)

    rate = rospy.Rate(10)

    msgs_pub = Mymsgs()

    while not rospy.is_shutdown():
    
        msgs_pub.x = 10
        msgs_pub.y = 10

        pub.publish(msgs_pub)

        rate.sleep()
