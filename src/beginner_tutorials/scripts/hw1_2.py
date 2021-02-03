#!/usr/bin/env python
import rospy
import geometry_msgs.msg, nav_msgs.msg

def callback(data):
    print data.twist.twist

def listener():

    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber('odometry/filtered',nav_msgs.msg.Odometry,callback)

    rospy.spin()

if __name__ == '__main__':
    listener()