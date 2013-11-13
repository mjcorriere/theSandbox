
from random import randint
from numpy import linalg
from matplotlib.pyplot import *

class Vertex(object):

	def __init__(self, _x, _y):

		self.x = _x
		self.y = _y

	def __str__(self):
		pass

class Edge(object):

	def __init__(self, _v0, _v1):

		self.v0 = _v0
		self.v1 = _v1

	def __str__(self):
		pass


class Hull(object):

	edgeList = []

	def __init__(self, _e0):

		edgeList.append(_e0)

	def __iter__(self):

		for edge in self.edgeList:
			yield edge

	def getEdgeGenerator(self):
		return iter(self).next

	def addEdge(E):

		edgeList.append(E)

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

def leftOfEdge(vertex, edge):

	vec1 = [edge.v0.x, edge.v0.y, 1]
	vec2 = [edge.v1.x, edge.v1.y, 1]
	vec3 = [vertex.x,  vertex.y,  1]

	M = [vec1] + [vec2] + [vec3]

	return linalg.det(M)
 
 
pc = PointCloud(30, [0, 50], [0, 50])

pairs = [(v.x, v.y) for v in pc]

data = zip(*pairs)
 
fig = figure()
ax = fig.add_subplot(111)

for n, pt in enumerate(pairs):
    ax.annotate(str(n), xy=pt, xytext=(3, 3),
                    textcoords='offset points')

ax.scatter(*data)
