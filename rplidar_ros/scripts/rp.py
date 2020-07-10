#!/usr/bin/env python

import rospy
from std_msgs.msg import String
from sensor_msgs.msg import LaserScan


def listener():

    rospy.init_node('rp', anonymous=True)

    rospy.Subscriber('scan', LaserScan, callback)

    rospy.spin()

def callback(data):
    for i in range (0, 359):
	lidar_dis1 = data.ranges[i]
	print("%dth value" %i, lidar_dis1)
    print('')

    for j in range (50, 70):
    lidar_dis2 = data.ranges[j]
    print("%dth value" %i, lidar_dis2)

    for k in range (90, 110):
    lidar_dis3 = data.ranges[k]

    for l in range (130, 150):
    lidar_dis4 = data.ranges[l]

if __name__ == '__main__':
    listener()









