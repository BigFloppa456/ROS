import numpy as np
import random
import math
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
# adapted from psuedo code in given link:
# https://theclassytim.medium.com/robotic-path-planning-rrt-and-rrt-212319121378

obstacles = np.array([ [0, 1.5], [0, 3], [0, 4.5], 
[1.5, 0], [1.5, 1.5], [1.5, 3], [1.5, 4.5],
[3, 0], [3, 1.5], [3, 3], [3, 4.5],
[4.5, 0], [4.5, 1.5], [4.5, 3], [4.5, 4.5] ],np.float32) #only centres right now
x=[]
y=[]

for i in range(len(obstacles)):
    x.append(obstacles[i][0])
    y.append(obstacles[i][1])
plt.scatter(x,y)




   
#Function declarations:


def shortest_distance(x1, y1, a, b, c):    
    d = abs((a * x1 + b * y1 + c)) / (math.sqrt(a * a + b * b))
    return d



def genNewConfig(goal):
     a = random.uniform(0,goal[0])
     b = random.uniform(0,goal[1])

     point = [a,b]
     return point

def Nearest(a, point):
    near = a[0]
    dist_near = math.sqrt((point[0] - near[0])**2 + (point[1] - near[1])**2)
    for pt in a:
        del_x = point[0] - pt[0]
        del_y = point[1] - pt[1]

        a = del_x**2
        b = del_y**2
        dist = math.sqrt(a+b)
        if dist < dist_near:
            near = pt
    return pt

def TRAVERSABLE(X,obs):
    x_nearest = Nearest(obs,X)
    dist = distance(x_nearest,X)

    if X in obs:
        return False
    #elif dist <= 0.25 :
    #    return False
    else:
        return True

def join(p1,p2):
    temp_x = []
    temp_y = []
    temp_x.append(p1[0])
    temp_x.append(p2[0])

    temp_y.append(p1[1])
    temp_y.append(p2[1])

    plt.plot(temp_x,temp_y)

def distance(p1,p2):
    del_x = p1[0] - p2[0]
    del_y = p1[1] - p2[1]

    a = del_x**2
    b = del_y**2
    dist = math.sqrt(a+b)

    return dist

#def path_dist(path):
#   for i in range(len(path)):



def RRT(start, goal,obst):
    radius = 0.25

    graph = []
    graph.append(start)
    
    #for x in range(100):
    for a in range(500):
        Xnew = genNewConfig(goal)

        if TRAVERSABLE(Xnew,obst)==False:
            continue
        
    
        x_nearest = Nearest(graph,Xnew)

        
        
        if (Xnew[0]>=x_nearest[0]) and (Xnew[1] >= x_nearest[1]):
            join(x_nearest,Xnew)
            graph.append(Xnew)
                


        #RRT(x_nearest,goal,obst)

        if Xnew in [goal]:
            #plt.show(block=True)
            graph.append(Xnew)
            #return graph
            
    #if distance(Xnew,goal)<distance(Xnew,x_nearest):
        #join(Xnew,goal)
            
    #plt.grid()
    #plt.show(block=True)
    return graph



"""S = [0,0]
G = [5,5]

path = RRT(S,G,obstacles) 

print (path)"""
