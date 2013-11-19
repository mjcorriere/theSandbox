
from random import randint
from numpy import linalg
from matplotlib.pyplot import *

class Vertex(object):

	def __init__(self, _x, _y):

		self.x = _x
		self.y = _y

		self.pair = (self.x, self.y)

	def __str__(self):
		return str( (self.x, self.y) )

	def __eq__(self, other):

		if self.x == other.x and self.y == other.y:
			return True
		else:
			return False

	def __ne__(self, other):
		
		if self.x == other.x and self.y == other.y:
			return False
		else:
			return True

class Edge(object):

	def __init__(self, _v0, _v1):

		self.v0 = _v0
		self.v1 = _v1

		self.pair = (self.v0.pair, self.v1.pair)

	def __str__(self):

		return str(self.v0) + ' ' + str(self.v1)

class Hull(object):

	edgeList = []

	def __init__(self, _e0):

		self.edgeList.append(_e0)

	def __iter__(self):

		for edge in self.edgeList:
			yield edge

	def getEdgeGenerator(self):
		return iter(self).next

	def addVertex(self, vertex):
		
		edgesToDelete = []

		for index, edge in enumerate(self.edgeList):

			if self.leftOfEdge(vertex, edge):
				continue
			else:
				edgesToDelete.append(index)

		if len(edgesToDelete) == 0:
			return False

		else:

			edgesToDelete.reverse()

			for index in edgesToDelete:
				del self.edgeList[index]

			# With edges deleted, we should have a hole in the hull.
			# Find out what that is.

			holeIndex = self.holeInHull()

			# We should make two new edges. From v1 of edge[holeIndex] to
			# vertex, and from vertex to edge[holeIndex + 1].
			# To preserve indicies, add the edges in CW order.

			edgeCW  = Edge(self.edgeList[holeIndex].v1, vertex)
			edgeCCW = Edge(vertex, self.edgeList[holeIndex + 1].v0)
			
			self.insertEdge(holeIndex + 1, edgeCCW)
			self.insertEdge(holeIndex + 1, edgeCW)

			return True

	def leftOfEdge(self, vertex, edge):
    
        	vec1 = [edge.v0.x, edge.v0.y, 1]
        	vec2 = [edge.v1.x, edge.v1.y, 1]
        	vec3 = [vertex.x,  vertex.y,  1]
        
        	M = [vec1] + [vec2] + [vec3]
    
        	return linalg.det(M) > 0

	def createInitialHull(self, vertex):

		# This is a bit of a hack as it doesn't take into account the
		# edge-case where the seedEdge happens to be on the outside
		# of the hull and facing away from the point cloud.

		if self.leftOfEdge(vertex, self.edgeList[0]):
		 	self.addEdge(Edge(self.edgeList[0].v1, vertex))
		 	self.addEdge(Edge(vertex, self.edgeList[0].v0))
		 	return True
		else:
		 	return False

	def addEdge(self, E):

		self.edgeList.append(E)

	def insertEdge(self, index, E):

		self.edgeList.insert(index, E)

	def holeInHull(self):
		"""
		Travels the hull in CCW order. Looks at edge[i]'s first vertex
		and compares with edge[i -1]'s second vertex. Returns the index
		of edge[i - 1] and the hole exists in the CCW direction of this
		edge.
		"""
		
		for index, edge in enumerate(self.edgeList):
			
			if edge.v0 == self.edgeList[index - 1].v1:
				continue
			else:
				print 'hole found at', index-1
				return index - 1

		return None

class PointCloud(object):

	def __init__(self, numPoints, xRange, yRange):

		self.vertexList = [Vertex(randint(*xRange), randint(*yRange)) \
								for n in range(numPoints)]

	def __iter__(self):

		for vertex in self.vertexList:
			yield vertex

	def getVertexGenerator(self):
		return iter(self).next
