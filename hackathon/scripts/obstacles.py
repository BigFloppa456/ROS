#!/usr/bin/env python

import rospy

import numpy as np
from hackathon.msg import centre
from std_msgs.msg import Float64MultiArray

centres = np.array( [[0, 1.5], [0, 3], [0, 4.5], [1.5, 0], [1.5, 1.5],[1.5, 3], [1.5, 4.5], [3, 0], [3, 1.5],[3, 3], [3, 4.5], [4.5, 0], [4.5, 1.5], [4.5,3], [4.5, 4.5]],np.float32 )



rospy.init_node('obstacles')

pub = rospy.Publisher('planner',centre,queue_size=1)
cent = centre()


for i in range(len(centres)):
	cent.x.append(centres[i][0])
	cent.y.append(centres[i][1])
rate = rospy.Rate(1)
while not rospy.is_shutdown():
	
	pub.publish(cent)	
	rate.sleep() 
		
"""pub = rospy.Publisher('planner',Float64MultiArray,queue_size=1)	
cent = Float64MultiArray()
cent.data = centres
rate = rospy.Rate(1)
while not rospy.is_shutdown():
	
	pub.publish(cent)	
	rate.sleep() """
