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
 
upperFrequency = 1 #Hz
lowerFrequency = 1 #Hz
numFrequencies = 5 
 
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
 
plt.plot(time, randomSignal)
 
#Frequency of interest!
fiIndex = 2
 
fi = freq[fiIndex] #Hz
fi_rad = fi * 2 * np.pi
 
theta = [fi_rad * t % (2*np.pi) for t in time]
 
xs = [randomSignal[i] * cos(theta[i]) for i in range(len(time))]
ys = [randomSignal[i] * sin(theta[i]) for i in range(len(time))]
 
x_avg = np.average(xs)
y_avg = np.average(ys)
 
plt.plot(xs, ys, linestyle='--')
plt.plot(x_avg, y_avg, marker='o', color='r')
plt.plot(0, 0, marker='o', color='g')
 
avg = sqrt(x_avg**2 + y_avg**2)
 
print "Avg distance from origin: ", avg
print "Half amplitude of freq of interest: ", amp[fiIndex] / 2
 
fig, ax = plt.subplots()
 
line, = ax.plot([], [], linestyle='-')
 
ax.set_ylim(-2, 2)
ax.set_xlim(-2, 2)
ax.grid()
ax.set_aspect(1)
 
xdata, ydata = [], []
 
def run(i):
 
    x = randomSignal[i] * cos(theta[i])
    y = randomSignal[i] * sin(theta[i])
 
    xdata.append(x)
    ydata.append(y)
 
    line.set_data(xdata, ydata)
 
    return line,
 
ani = animation.FuncAnimation(fig, run, frames=len(time), blit=True,
                               interval=20, repeat=False)
 
plt.show()

