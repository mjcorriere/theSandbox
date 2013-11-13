from random import randint
from numpy import linalg
from matplotlib.pyplot import *

class Vertex(object):

	def __init__(self, _x, _y):

		self.x = _x
		self.y = _y

	def __str__(self):
		return str((self.x, self.y))

class Edge(object):

	def __init__(self, _v0, _v1):

          self.v0 = _v0
          self.v1 = _v1

	def __str__(self):
     
          v0 = (self.v0.x, self.v0.y)
          v1 = (self.v1.x, self.v1.y)
         
          return 'v0: ' + str(v0) + ' v1: ' + str(v1)

class Hull(object):

#	edgeList = []

	def __init__(self, _e0):
         self.edgeList = []
         self.edgeList.append(_e0)

	def __iter__(self):

		for edge in self.edgeList:
			yield edge

	def getEdgeGenerator(self):
		return iter(self).next
  
	def getVisibleEdges(self, vertex):
            
		visibleEdges = []
          
		for index, edge in enumerate(self.edgeList):

			vec1 = [edge.v0.x, edge.v0.y, 1]
			vec2 = [edge.v1.x, edge.v1.y, 1]
			vec3 = [vertex.x,  vertex.y,  1]
            
			M = [vec1] + [vec2] + [vec3]
            
			if linalg.det(M) > 0:
				visibleEdges.append(index)
    
		return visibleEdges
               
	def addEdge(E):

		self.edgeList.append(E)

class PointCloud(object):

	vertexList = []

	def __init__(self, numPoints, xRange, yRange):

		self.vertexList = [Vertex(randint(*xRange), randint(*yRange)) \
								for n in range(numPoints)]

	def __iter__(self):

		for vertex in self.vertexList:
			yield vertex

	def getVertexGenerator(self):
		return iter(self).next