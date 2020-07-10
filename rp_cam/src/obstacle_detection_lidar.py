#!/usr/bin/env python
from __future__ import print_function

import roslib
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import Float64
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
class lidar_data:

  def __init__(self):
    # self.image_pub = rospy.Publisher("image_topic_2",Image)
    self.rate = rospy.Rate(20)
    self.bridge = CvBridge()
    self.timer_to_sending_data = 0
    

    self.speed = rospy.Publisher('/cmd_vel', Twist, queue_size=1) 
    self.move_cmd = Twist()  
    self.linear_speed = 0.1
    self.angular_speed = 0.0
    # self.speed_value = 1200
    # self.position_value = 0.5
   # self.speed.publish(0.0)
    # self.position.publish(self.position_value)
    self.image_sub = rospy.Subscriber("/usb_cam/image_raw",Image,self.callback)
    self.scan_sub = rospy.Subscriber("/scan",LaserScan,self.find_distance)
    # rospy.on_shutdown(self.shutdown)


  def callback(self,data):
    self.rate.sleep()
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
      cv2.imshow("Image",cv_image)
    except CvBridgeError as e:
      print(e)
    
  def find_distance(self,data):
    for i in range(0,10):
        self.lidar_dist = data.ranges[i]
        print("Distance:",self.lidar_dist)

        if self.lidar_dist != float("inf"):
            self.lidar_front_dist = data.ranges[0]
            self.lidar_front_left = data.ranges[20]
            print("front",self.lidar_front_dist)
            if self.lidar_front_dist > 0.3:
              self.move_cmd.linear.x = self.linear_speed
              # self.position.publish(self.position_value)
              self.speed.publish(self.move_cmd)
            # else:
            #   while self.count<2:
            #       self.speed_value = 1000
            #       self.speed.publish(self.speed_value)
            #       self.position_value = 1.0
            #       self.position.publish(self.position_value)
            #       self.lidar_front_left = data.ranges[190]
            #       self.count+=1
            #   if self.lidar_front_left <0.2:
            #     self.speed_value = 800
            #     self.speed.publish(self.speed_value)
            # self.count

        else:
          print("Not in range")
          self.move_cmd.linear.x = 0.0
          self.speed.publish(self.move_cmd)
      
    self.timer_to_sending_data += 1
    
  # def shutdown(self):
  #   self.speed.publish(0)
  #   self.position.publish(0.4)
  #   self.rate.sleep()

def main(args):
  

  rospy.init_node('image_converter', anonymous=True)
  

  ld = lidar_data()
    
  rospy.spin()

if __name__ == '__main__':
    main(sys.argv)
