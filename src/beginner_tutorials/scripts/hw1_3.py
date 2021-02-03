#!/usr/bin/env python
import rospy
from std_msgs.msg import String
import geometry_msgs.msg, nav_msgs.msg, sensor_msgs.msg
import math 

def callback(data):
    angle_min = math.degrees(data.angle_min)  
    angle_max = math.degrees(data.angle_max)  
    angle_increment = math.degrees(data.angle_increment) 
    range_min = data.range_min  
    range_max = data.range_max  
    dist_angle_min = data.ranges[0]  
    num_scan = len(data.ranges)
    
    print "num_scan = ", num_scan
    print angle_min, angle_max, angle_increment, range_min, range_max, dist_angle_min


def listener():

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('scan',sensor_msgs.msg.LaserScan,callback)

    rospy.spin()

if __name__ == '__main__':
    listener()