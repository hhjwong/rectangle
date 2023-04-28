import numpy as np
from matplotlib import pyplot as plt
import math 
from math import sqrt
import random
import array as arr
from matplotlib.patches import Rectangle
import pylab as pl
from matplotlib import collections  as mc
from numpy import sin, cos, pi, linspace
from datetime import datetime

def ABS_Dist(x1,x2,y1,y2):
    result=sqrt((x1 - x2)**2 + (y1 - y2)**2)
    #print(result)
    return result
def onSegment(px,py,qx,qy,rx,ry):
    if qx<= max(px,rx) and qx >= min(px,rx) and qy <= max(py,ry) and qy >= min(py,ry):
        return True
    return False

def orientation(px,py,qx,qy,rx,ry):
    val=(qy-py)*(rx-qx)-(qx-px)*(ry-qy)
    if val>0:
        return 1
    elif val<0:
        return 2
    else:
        return 0

def intersection_check(p1x,p1y,q1x,q1y,p2x,p2y,q2x,q2y):
    o1=orientation(p1x,p1y,q1x,q1y,p2x,p2y)
    o2=orientation(p1x,p1y,q1x,q1y,q2x,q2y)
    o3=orientation(p2x,p2y,q2x,q2y,p1x,p1y)
    o4=orientation(p2x,p2y,q2x,q2y,q1x,q1y)
    if o1 != o2 and o3 != o4:
        return True
    if o1==0 and onSegment(p1x,p1y,p2x,p2y,q1x,q1y):
        return True
    if o2==0 and onSegment(p1x,p1y,q2x,q2y,q1x,q1y):
        return True
    if o3==0 and onSegment(p2x,p2y,p1x,p1y,q2x,q2y):
        return True
    if o1==0 and onSegment(p2x,p2y,q1x,q1y,q2x,q2y):
        return True
    return False
def intersection_test(p1x,p1y,q1x,q1y):
    valid=False
    for x in range (34):
        #print("kill", x)
        valid=intersection_check(p1x,p1y,q1x,q1y,edge[x,0,0],edge[x,0,1],edge[x,1,0],edge[x,1,1])
        if valid==True:
            return False
    return True
    
random.seed(datetime.now().timestamp())
#edge [x1,y1,x2,y2]
edge=[[(0.3,0.3),(8,0.3)], [(8.8,0.3),(10.8,0.3)], [(10.8,0.3),(10.8,5.3)], [(10.1,5.3),(10.8,5.3)], [(10.1,5.3),(10.1,6.3)], [(0.3,6.3),(10.1,6.3)], [(0.3,0.3),(0.3,6.3)], [(0,0),(8,0)], [(8,0),(8,0.3)], [(8.8,0),(8.8,0.3)], [(8.8,0),(11.1,0)], [(0,6.6),(11.1,6.6)], [(11.1,0),(11.1,6.6)], [(2.5,2),(8,2)], [(2.5,2),(2.5,2.5)], [(2.5,2.5),(7.5,2.5)], [(7.5,2.5),(7.5,3.5)], [(2.5,3.5),(7.5,3.5)], [(2.5,3.5),(2.5,4)], [(2.5,4),(7.5,4)], [(7.5,4),(7.5,5)], [(2.5,5),(7.5,5)], [(2.5,5),(2.5,5.5)], [(2.5,5.5),(8,5.5)], [(8,2),(8,5.5)], [(-2,-2),(11.1,-2)], [(11.1,-2),(11.1,-2.3)], [(-2.3,-2.3),(-2.3,6.6)], [(-2,-2),(-2,6.6)], [(-2.3,6.6),(-2,6.6)], [(0,0),(0,6.6)], [(-2.3,-2.3),(11.1,-2.3)], [(-2,6.6),(0,6.6)], [(11.1,-2),(11.1,0)]]
edge=np.array(edge)
sprawn=[[8.4,0.5], [6,1.6], [3,1.6], [3,3], [6,3], [3,4.5], [6.,4.5], [3,5.8], [6,5.8], [10,4], [10,2], [-1.3,-1.3], [1,4], [5,-1], [-1,5]]
sprawn=np.array(sprawn)
#ax=plt.subplot(1,1,1)
user_loc=np.zeros((10,2),dtype=float)
#choose 10 out of 15 location to activate
chosen_loc = random.sample(range(1, 15), 10)
for x in range (0,10):
    user_loc[x,0]=sprawn[chosen_loc[x],0]
    user_loc[x,1]=sprawn[chosen_loc[x],1]
duration=10 #sampling duration (1/sampling rate)
T_time=10
counter=10
all_loc=np.zeros((duration*T_time*10,2),dtype=float)
direction=np.zeros(10,dtype=int)
for x in range(10):
    all_loc[x,0]=user_loc[x,0]
    all_loc[x,1]=user_loc[x,1]
for x in range(1,T_time*duration):
    if x%100==0:
        print(x)
    for y in range (0,10):
        speed=np.random.normal(0.0,2.0)
        direction[y]=random.randint(1,8)
            #print(y,"	",direction[y])
        passed=False
        #print(x,"\t",y)
        while not passed:
            if direction[y]==1:
                passed=intersection_test(user_loc[y,0],user_loc[y,1],user_loc[y,0]+speed/duration,user_loc[y,1])
                #print(passed)
                if not passed:
                    direction[y]=random.randint(1,8)
                    #print(y,"	",direction[y])
                else:
                    all_loc[counter,0]=user_loc[y,0]+speed/duration
                    all_loc[counter,1]=user_loc[y,1]
                    user_loc[y,0]=all_loc[counter,0]
                    user_loc[y,1]=all_loc[counter,1]
                    counter+=1
            elif direction[y]==2:
                passed=intersection_test(user_loc[y,0],user_loc[y,1],user_loc[y,0]+0.707*speed/duration,user_loc[y,1]+0.707*speed/duration)
                #print(passed)
                if not passed:
                    direction[y]=random.randint(1,8)
                    #print(y,"	",direction[y])
                else:
                    all_loc[counter,0]=user_loc[y,0]+0.707*speed/duration
                    all_loc[counter,1]=user_loc[y,1]+0.707*speed/duration
                    user_loc[y,0]=all_loc[counter,0]
                    user_loc[y,1]=all_loc[counter,1]
                    counter+=1
            elif direction[y]==3:
                passed=intersection_test(user_loc[y,0],user_loc[y,1],user_loc[y,0],user_loc[y,1]+speed/duration)
                #print(passed)
                if not passed:
                    direction[y]=random.randint(1,8)
                    #print(y,"	",direction[y])
                else:
                    all_loc[counter,0]=user_loc[y,0]
                    all_loc[counter,1]=user_loc[y,1]+speed/duration
                    user_loc[y,0]=all_loc[counter,0]
                    user_loc[y,1]=all_loc[counter,1]
            elif direction[y]==4:
                passed=intersection_test(user_loc[y,0],user_loc[y,1],user_loc[y,0]-0.707*speed/duration,user_loc[y,1]+0.707*speed/duration)
                #print(passed)
                if not passed:
                    direction[y]=random.randint(1,8)
                    #print(y,"	",direction[y])
                else:
                    all_loc[counter,0]=user_loc[y,0]-0.707*speed/duration
                    all_loc[counter,1]=user_loc[y,1]+0.707*speed/duration
                    user_loc[y,0]=all_loc[counter,0]
                    user_loc[y,1]=all_loc[counter,1]
                    counter+=1
            elif direction[y]==5:
                passed=intersection_test(user_loc[y,0],user_loc[y,1],user_loc[y,0]-speed/duration,user_loc[y,1])
                #print(passed)
                if not passed:
                    direction[y]=random.randint(1,8)
                    #print(y,"	",direction[y])
                else:
                    all_loc[counter,0]=user_loc[y,0]-speed/duration
                    all_loc[counter,1]=user_loc[y,1]
                    user_loc[y,0]=all_loc[counter,0]
                    user_loc[y,1]=all_loc[counter,1]
                    counter+=1
            elif direction[y]==6:
                passed=intersection_test(user_loc[y,0],user_loc[y,1],user_loc[y,0]-0.707*speed/duration,user_loc[y,1]-0.707*speed/duration)
                #print(passed)
                if not passed:
                    direction[y]=random.randint(1,8)
                    #print(y,"	",direction[y])
                else:
                    all_loc[counter,0]=user_loc[y,0]-0.707*speed/duration
                    all_loc[counter,1]=user_loc[y,1]-0.707*speed/duration
                    user_loc[y,0]=all_loc[counter,0]
                    user_loc[y,1]=all_loc[counter,1]
                    counter+=1
            elif direction[y]==7:
                passed=intersection_test(user_loc[y,0],user_loc[y,1],user_loc[y,0],user_loc[y,1]-speed/duration)
                #print(passed)
                if not passed:
                    direction[y]=random.randint(1,8)
                    #print(y,"	",direction[y])
                else:
                    all_loc[counter,0]=user_loc[y,0]
                    all_loc[counter,1]=user_loc[y,1]-speed/duration
                    user_loc[y,0]=all_loc[counter,0]
                    user_loc[y,1]=all_loc[counter,1]
                    counter+=1
            elif direction[y]==8:
                passed=intersection_test(user_loc[y,0],user_loc[y,1],user_loc[y,0]+0.707*speed/duration,user_loc[y,1]-0.707*speed/duration)
                #print(passed)
                if not passed:
                    direction[y]=random.randint(1,8)
                    #print(y,"	",direction[y])
                else:
                    all_loc[counter,0]=user_loc[y,0]+0.707*speed/duration
                    all_loc[counter,1]=user_loc[y,1]-0.707*speed/duration
                    user_loc[y,0]=all_loc[counter,0]
                    user_loc[y,1]=all_loc[counter,1]
                    counter+=1
                    
for x in range (0,duration*10*T_time):
    angle_error=np.random.normal(0.0,360.0)
    length_error=np.random.normal(0.0,0.1)
    x_error=math.cos(math.radians(angle_error))*length_error
    y_error=math.sin(math.radians(angle_error))*length_error
    all_loc[x,0]+=x_error
    all_loc[x,1]+=y_error

grid=np.zeros((890,1340),dtype=int)
g_truth=np.zeros((890,1340),dtype=int)
for m in range (0,30):
    for n in range(0,890):
        g_truth[n,m]=200
for m in range (0,1340):
    for n in range(0,30):
        g_truth[n,m]=200
for m in range (230,260):
    for n in range(230,890):
        g_truth[n,m]=200
for m in range (230,1030):
    for n in range(230,260):
        g_truth[n,m]=200
for m in range (230,1240):
    for n in range(860,890):
        g_truth[n,m]=200
for m in range (1240,1340):
    for n in range(760,890):
        g_truth[n,m]=200
for m in range (1310,1340):
    for n in range(230,760):
        g_truth[n,m]=200
for m in range (1110,1340):
    for n in range(230,260):
        g_truth[n,m]=200
for m in range (480,980):
    for n in range(430,480):
        g_truth[n,m]=200
for m in range (480,980):
    for n in range(580,630):
        g_truth[n,m]=200
for m in range (480,980):
    for n in range(730,780):
        g_truth[n,m]=200
for m in range (980,1030):
    for n in range(430,780):
        g_truth[n,m]=200

threshold_val=1.3
for x in range (0,duration*10*T_time):
    if x%100==0:
        print(x)
    for y in range (x,duration*10*T_time):
        check=ABS_Dist(all_loc[x,0],all_loc[y,0],all_loc[x,1],all_loc[y,1])
        if check<(threshold_val*2/duration):
            #print(check,all_loc[x],all_loc[y])
            if all_loc[x,0]>all_loc[y,0] and all_loc[x,1]>all_loc[y,1]:
                start_x=int(round(all_loc[y,0]*100))+230
                start_y=int(round(all_loc[y,1]*100))+230
                end_x=int(round(all_loc[x,0]*100))+230
                end_y=int(round(all_loc[x,1]*100))+230
                for m in range(max(start_x,0),min(end_x,1340)):
                    for n in range(max(start_y,0),min(end_y,890)):
                        grid[n,m]=200
            elif all_loc[x,0]<all_loc[y,0] and all_loc[x,1]>all_loc[y,1]:
                start_x=int(round(all_loc[x,0]*100))+230
                start_y=int(round(all_loc[y,1]*100))+230
                end_x=int(round(all_loc[y,0]*100))+230
                end_y=int(round(all_loc[x,1]*100))+230
                for m in range(max(start_x,0),min(end_x,1340)):
                    for n in range(max(start_y,0),min(end_y,890)):
                        grid[n,m]=200
            elif all_loc[x,0]>all_loc[x,0] and all_loc[x,1]<all_loc[y,1]:
                start_x=int(round(all_loc[y,0]*100))+230
                start_y=int(round(all_loc[x,1]*100))+230
                end_x=int(round(all_loc[x,0]*100))+230
                end_y=int(round(all_loc[y,1]*100))+230
                for m in range(max(start_x,0),min(end_x,1340)):
                    for n in range(max(start_y,0),min(end_y,890)):
                        grid[n,m]=200
            elif all_loc[x,0]<all_loc[y,0] and all_loc[x,1]<all_loc[y,1]:
                start_x=int(round(all_loc[x,0]*100))+230
                start_y=int(round(all_loc[x,1]*100))+230
                end_x=int(round(all_loc[y,0]*100))+230
                end_y=int(round(all_loc[y,1]*100))+230
                for m in range(max(start_x,0),min(end_x,1340)):
                    for n in range(max(start_y,0),min(end_y,890)):
                        grid[n,m]=200

positive=0 #accessible
negative=0 # obstacles
true_positive=0
true_negative=0
for m in range(0,1340):
    for n in range(0,890):
        if g_truth[n,m]==200:
            negative+=1
            if grid[n,m]==0:
                true_negative+=1
        if g_truth[n,m]==0:
            positive+=1
            if grid[n,m]==200:
                true_positive+=1
print("Accessible area accuracy: ",float(true_positive/positive))
print("Obstacle area accuracy: ",float(true_negative/negative))
print("Total accuracy: ",float((true_positive+true_negative)/(positive+negative)))
plt.imshow(grid,cmap='Blues',origin='lower')
np.save("result.npy",grid)
plt.show()

