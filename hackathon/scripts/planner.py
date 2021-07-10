#!/usr/bin/env python

import rospy
import numpy as np
from hackathon.msg import centre
import RRT_test

import random
import math
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

radius = 0.25



def plot(msg):
    """arr = np.arr([],np.float64)
    for i in range(len(msg.x)):
        np.append(arr,[msg.x[i],msg.y[i]])"""
    plt.scatter(msg.x, msg.y)



    obstacles =[]
    for i in range(len(msg.x)):
      obstacles.append([msg.x[i],msg.y[i]])

    start = [0,0]
    goal_x = int(input("Enter a goal x coord: "))
    goal_y = int(input("Enter a goal y coord: "))

    goal = [goal_x,goal_y]

    path = RRT_test.RRT(start,goal,obstacles)

    path_x = []
    path_y = []

    for i in range(len(path)):
        path_x.append(path[i][0])
        path_y.append(path[i][1])

    #ret_path = centre()

    ret_path.x = path_x
    ret_path.y = path_y

    rate=rospy.Rate(2)

    while not rospy.is_shutdown():
        pub.publish(ret_path)
        rate.sleep()


    plt.show(block=True)


rospy.init_node('path')

sub = rospy.Subscriber('planner',centre,plot)

pub = rospy.Publisher('path_list',centre,queue_size=1)

ret_path = centre()


rospy.spin()