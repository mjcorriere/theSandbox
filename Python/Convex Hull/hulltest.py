# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 17:04:50 2013

@author: mcorriere
"""

import convexhull_v2 as chull
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import csv

from itertools import chain

xRange = [0, 100]
yRange = [0, 100]

pointCloud = chull.PointCloud(100, xRange, yRange)

## <hackish>
## This should be cleaned up.

## FIX: Add the first edge in -both- directions. This way, one is guaranteed
## to be deleted and the hull can continue as normal. This whole part can then
## disappear.
vtxGenerator = pointCloud.getVertexGenerator()

seedEdge = chull.Edge(vtxGenerator(), vtxGenerator())

hull = chull.Hull(seedEdge)

loop = False

while not loop:
    loop = hull.createInitialHull(vtxGenerator())
    
## </hackish>

for point in pointCloud:
    
    hull.addVertex(point)

    
## Hull complete at this point. Remainder here is for plotting    
    
points = [p.pair for p in pointCloud]

plt.scatter(*zip(*points))


## These next lines can probably be done more intelligently / in less lines
edges = [edge.pair for edge in hull]

xs, ys = [], []

for edge in edges:

    xs += zip(*edge)[0]
    ys += zip(*edge)[1]    
    
def data_gen():
    for x, y in zip(xs, ys):
        yield x, y

#fig, ax = plt.subplots()

fig = plt.gcf()
ax = plt.gca()
line, = ax.plot([], [], lw=2)

ax.set_xlim(*xRange)
ax.set_ylim(*yRange)

ax.grid()

xdata, ydata = [], []

def run(data):
    # update the data
    xn, yn = data    
    xdata.append(xn)
    ydata.append(yn)

    line.set_data(xdata, ydata)

    return line,

ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=500,
    repeat=False)

plt.show()

def writeToFiles(pointFileName, edgeFileName):
    
    pointFile = open(pointFileName, 'wb')
    edgeFile = open(edgeFileName, 'wb')
    
    pointFile.write('xs,ys\n')
    edgeFile.write('xs,ys\n')    
    
    pfwrite = csv.writer(pointFile, delimiter=',')
    efwrite = csv.writer(edgeFile, delimiter=',')
    
    for point in points:
        pfwrite.writerow(point)
        
    edgesFlat = list(chain(*edges))
        
    for edge in edgesFlat:
        efwrite.writerow(edge)
        
    pointFile.close()
    edgeFile.close()