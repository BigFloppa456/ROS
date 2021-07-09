#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist

rospy.init_node('vel_pub')

move = Twist()

move.linear.x=1
move.angular.z=1
pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)





rate=rospy.Rate(2)

while not rospy.is_shutdown():
    pub.publish(move)
    rate.sleep()
