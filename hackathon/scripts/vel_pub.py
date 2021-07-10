#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from hackathon.msg import centre


def func(msg):
    for i in range(len(msg.x)):

        move.linear.x = msg.x[i]
        move.linear.y = msg.y[i]
        
        
        rate=rospy.Rate(2)

        while not rospy.is_shutdown():
            pub.publish(move)
            rate.sleep()









rospy.init_node('vel_pub')

move = Twist()

"""move.linear.x=1
move.angular.z=1"""
sub = rospy.Subscriber('path_list',centre,func)
pub = rospy.Publisher('/cmd_vel',Twist,queue_size=1)







rospy.spin()
