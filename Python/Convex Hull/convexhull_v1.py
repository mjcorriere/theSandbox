# -*- coding: utf-8 -*-
"""
Created on Sun Nov 03 13:28:27 2013

@author: NotMark

An implementation of the convex hull algorithm done by the Increment method.
Implemented based on writeup at 
    http://www.cse.unsw.edu.au/~lambert/java/3d/incremental.html
    

"""

from random import randint
from matplotlib import pyplot as plt
from numpy.linalg import det
import numpy as np


def generatePointCloud(numPoints, width, height):
    """
    Returns a list of 2-tuples numPoints long. Each tuple contains a random x 
    value and a random y value between width and height, respectively.
    """    
    
    return [(randint(0, width), randint(0, height)) for n in range(numPoints)]
    
class Edge(object):

    p0 = p1 = 0
    
    def __init__(self, _p0, _p1):
        self.p0 = _p0
        self.p1 = _p1    

class EdgeList(object):
    
    edgeList = []
    
    def __init__(self):
        pass
        
    def addEdge(self, edge):
        edgeList.append(edge)
    
def argtest(*args):
    print args
    
def plotArrow(p0, p1, headWidth=.1):
    
    dx = p1[0] - p0[0]
    dy = p1[1] - p0[1]
    
    plt.arrow(p0[0], p0[1], dx, dy, head_width=headWidth, 
                  length_includes_head = True)

# *pointCloud takes every element of pointCloud and splits it into an
# argument of zip. This is equivalent to calling zip((a,b), (c, d), (e, f))
# which would result in (a, c, e), (b, d, f). Zip combines all the first
# elements of a list of lists and puts it into list 1. Then the second into
# list 2, etc.

# Putting this all together, calling zip(*pointCloud) gives us a list of two
# long tuples. The first tuple contains all the x values, the second tuple
# all the y values. If we use the splat operator on this new list, we pass
# plt.scatter TWO DISTINCT TUPLES, one of x and one of y values. Bingo.

pointCloud = generatePointCloud(50, 400, 600)

edgeList = []

# Make the very first edge manually

edgeList.append([pointCloud.pop(0), pointCloud.pop(0)])

# Using pop is a way to circumvent having to keeping track of the point index
# Tihs could possibly be handled better.

# Lets create our initial triangle. This will be a special case of the
# algorithm where we are looking for a positive value of the determinant.
# this will give us a nice CCW hull to start from.

for index, point in enumerate(pointCloud):
    
    p0 = edgeList[0][0]
    p1 = edgeList[0][1]
    
    array = np.array([p0 + (1,), p1 + (1,), point + (1,)])
    
    determinant = det(array)
    
    if determinant > 0:
        edgeList.append([p1, point])
        edgeList.append([point, p0])
        pointCloud.pop(index)        
        break        
    
for pointIndex, point in enumerate(pointCloud):
    
    edgeIndiciesToDelete = []
    
    for edgeIndex, edge in enumerate(edgeList):
        
        array = np.array([edge[0] + (1,), edge[1] + (1,), point + (1,)])
        
        determinant = det(array)
        
        if determinant < 0:
            #Mark it for deletion
            edgeList[edgeIndex] = '!'
            edgeIndiciesToDelete.append(edgeIndex)
            
            
    # If there are no edges to delete, the point must be inside the hull.
    # Move onto the next point.
    
    print str(edgeList)
    numEdgesToDelete = edgeList.count('!')
    
    if numEdgesToDelete == 0:
        print 'Nothing to delete!'
        continue
    
    # Otherwise ...    
    # Add fresh edges
    
    numEdges = len(edgeList)
    wrapEvent = False
    
    numEdgesToDelete = len(edgeIndiciesToDelete)

    for i in range(numEdgesToDelete - 1):
        if (edgeIndiciesToDelete[i + 1] - edgeIndiciesToDelete[i]) != 1:
            wrapEvent = True
            break
        
    if wrapEvent:
        prevEdgeIndex = (max(edgeIndiciesToDelete) - 1) % numEdges
        nextEdgeIndex = (min(edgeIndiciesToDelete) + 1) % numEdges 
            
    else:
        prevEdgeIndex = (min(edgeIndiciesToDelete) - 1) % numEdges
        nextEdgeIndex = (max(edgeIndiciesToDelete) + 1) % numEdges

    cwEdge = edgeList[ prevEdgeIndex ]
    ccwEdge = edgeList[ nextEdgeIndex ]

    """
    THE PROBLEM LIES IN HERE. CLEAN UP YOUR CODE AND MAKE SURE YOU ARE
    REFERENCING WHAT YOU THINK YOU ARE REFERENCING.
    
    REFERRING TO [-1] AND [0] ARE STATIC ABSOLUTE REFERENCES. THEY MUST ADJUST
    TO THE SITUATION AT HAND.
    """

    print 'Adding edge2 ...'    
    edgeList.insert(edgeIndiciesToDelete[-1], [point, ccwEdge[0]])
    ###edgeList.insert(nextEdgeIndex - 1, [point, ccwEdge[0]])    

    print 'Adding edge1 ...'    
    edgeList.insert(edgeIndiciesToDelete[0], [cwEdge[1], point])       
    ###edgeList.insert(prevEdgeIndex + 1, [cwEdge[1], point])   
    
    
    # Delete the offending edges

    for i in range(numEdgesToDelete):
        edgeList.remove('!')


# Plot the results

plt.xlim([-50, 450])
plt.ylim([-50, 650])

plt.scatter(*zip(*pointCloud))
    
for edge in edgeList:
    plotArrow(*edge, headWidth=15)
    
"""
What datastructures do I need?

I need a list of my points. I will increment through this list of points with
a point index. This point index will always go up. I don't need to keep track
of which points are in the hull or not. This is implied by the edges. Edges
have points. Hulls have edges.

An edge should be stored as two points. The points are stored in an order such
that they imply a direction. The first point is the tail of the edge vector,
the second point is the tip. i.e. [(tip), (tail)]. This will make ordering in
the hull easier.

The hull is a list of these edges stored in counterclockwise (CCW) order. CCW 
order for the hull means that if I take the determinant of the 3 points forming
any two adjacent edges, I should get a positive value.

Pseudocode

for point in pointlist:
    
    for edge in edgelist:
        
        determinant of (edge P0, edge P1, and point)
        
        if determinant is negative:
            mark this edge for deletion
            
    if no edges marked for deletion:
        skip to next point (break this loop iteration)
    
    delete visible edges
    
    attach CW-most open edge to point
    attach point to CCW-most open edge
    
    continue

"""