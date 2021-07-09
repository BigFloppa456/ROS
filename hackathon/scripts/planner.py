#!/usr/bin/env python

import rospy
import numpy as np
from hackathon.msg import centre

import random
import math
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

radius = 0.25
"""x = None
y = None"""
def plot(msg):
    """arr = np.arr([],np.float64)
    for i in range(len(msg.x)):
        np.append(arr,[msg.x[i],msg.y[i]])"""
    plt.scatter(msg.x, msg.y)
    global x 
    global y 
    x = msg.x
    y = msg.y
    plt.show(block=True)
    
   

"""def RRT(start,goal):
    tree =[]
    tree.append(start)"""


rospy.init_node('path')

sub = rospy.Subscriber('planner',centre,plot)
print(x)

rospy.spin()