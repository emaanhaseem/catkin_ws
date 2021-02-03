#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist

def move_circle():

    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=1)
     
    cmd_msg = Twist()
    cmd_msg.linear.x = 0.5

    rospy.init_node('keep_moving', anonymous=True)
    now = rospy.Time.now()
    rate = rospy.Rate(10)


    while not rospy.is_shutdown():
        pub.publish(cmd_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        move_circle()
    except rospy.ROSInterruptException:
        pass
