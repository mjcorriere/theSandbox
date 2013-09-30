# -*- coding: utf-8 -*-
"""
Created on Tue Sep 03 17:11:29 2013

@author: Mark
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 03 11:46:09 2013
 
@author: mcorriere
"""
 
import numpy as np
import matplotlib.pyplot as plt

from numpy.random import rand
from math import sin, cos, sqrt

import matplotlib.animation as animation
 
upperFrequency = 5 #Hz
lowerFrequency = 5  #Hz
numFrequencies = 1
 
timeWindow = 1 #sec
timeStep = .001
 
time = np.linspace(0, timeWindow - timeStep, timeWindow/timeStep)
 
freq = np.linspace(lowerFrequency, upperFrequency, numFrequencies).tolist()
 
omega = [2 * np.pi * f for f in freq]
 
phase = []
amp   = []
 
for n in range(numFrequencies):
   
    phase.append(2 * np.pi * rand())
    amp.append(rand())
   
randomSignal = []
temp = []
 
for t in time:
       
    for n in range(numFrequencies):
       
        temp.append( amp[n] * sin (omega[n] * t - phase[n]))
       
    randomSignal.append(sum(temp))    
       
    temp = []
 
plt.figure(1)
plt.plot(time, randomSignal)
 
#Frequency of interest!
fiIndex = 0
 
#fi = freq[fiIndex] #Hz
fi = 5
fi_rad = fi * 2 * np.pi
 
theta = [fi_rad * t % (2*np.pi) for t in time]
 
xs = [randomSignal[i] * cos(theta[i]) for i in range(len(time))]
ys = [randomSignal[i] * sin(theta[i]) for i in range(len(time))]
 
x_avg = np.average(xs)
y_avg = np.average(ys)

plt.figure(2)

plt.plot(xs, ys, linestyle='--')
plt.plot(x_avg, y_avg, marker='o', color='r')
plt.plot(0, 0, marker='o', color='g')
 
avg = sqrt(x_avg**2 + y_avg**2)
 
print "Avg distance from origin: ", avg
print "Half amplitude of freq of interest: ", amp[ fiIndex] / 2

fig, (ax1, ax2) = plt.subplots(2, 1)


line, = ax1.plot([], [], linewidth=1, linestyle='-')
line2, = ax2.plot([], [])

ax1.set_ylim(-2, 2)
ax1.set_xlim(-2, 2)
ax1.set_aspect(1)

ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')

ax1.xaxis.set_ticks_position('bottom')
ax1.spines['bottom'].set_position(('data', 0))

ax1.yaxis.set_ticks_position('left')
ax1.spines['left'].set_position(('data', 0))

pltmax = max([abs(min(xs + ys)), max(xs + ys)]) * 1.1

ax1.set_xlim(-pltmax, pltmax)
ax1.set_ylim(-pltmax, pltmax)

ax2.set_xlim(0, .5)
ax2.set_ylim(-1, 1)

xdata, ydata = [], []

temp = []
mySignal = []
myTime = []

t = 0.0

tmax = .5

print "running "

def run(i):

    global temp, mySignal, myTime, t    
    
    myTime.append(t)

    for n in range(numFrequencies):
       
        temp.append( amp[n] * sin (omega[n] * time[i] - phase[n]))
       
    mySignal.append(sum(temp))    
       
    temp = []
    
    t += timeStep

    x = randomSignal[i] * cos(theta[i])
    y = randomSignal[i] * sin(theta[i])

    xdata.append(x)
    ydata.append(y)
    
    print "i ", i

    line.set_data(xdata, ydata)
    print "first line set"    
    
#    print time[:i+1]
#    print mySignal
    
    line2.set_data(myTime, mySignal)
    
    if t >= tmax-.1:
        line2.axes.set_xlim(t - tmax +.1, t + .1)

    return line, line2

ani = animation.FuncAnimation(fig, run, frames=100, blit=True, 
                               interval=60, repeat=False)

#plt.show()

