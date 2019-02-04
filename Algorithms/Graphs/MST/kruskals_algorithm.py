"""
Kruskal's Algorithm for Adjacency Matrix
"""
from collections import defaultdict


class Graph:
				
				def __init__(self, vertices):
								self.V = vertices #No. of vertices
								self.graph = [] #Default dict to store graph
								
				def add_edge(self, u, v, w):
								self.graph.append([u, v, w])
								
				def find(self, parent, i):
								if parent[i] == i:
												return i
								
								return self.find(parent, parent[i])
				
				def union(self, parent, rank, x, y):
								xroot = self.find(parent, x)
								yroot = self.find(parent, y)
								
								if rank[xroot] < rank[yroot]:
												parent[xroot] = yroot
								elif rank[xroot] > rank[yroot]:
												parent[yroot] = xroot
								else:
												parent[yroot] = xroot
												rank[xroot] += 1
								
				def kruskalmst(self):
								
								result = []
								i, e = 0, 0
								
								#Step 1. Sort all edges in Non decreasing order of their weight
								self.graph = sorted(self.graph, key=lambda item: item[2])
								parent = []
								rank = []
								
								#Create V Subsets with single elements
								for node in range(self.V):
												parent.append(node)
												rank.append(0)
								
								#Number of edges to be taken is equal to V-1
								while e < self.V - 1:
												#Step 2. Pick the smallest edge and increment the index for next iteration
												u, v, w = self.graph[i]
												i = i+1
												x = self.find(parent, u)
												y = self.find(parent, v)
												
												if x != y:
																e = e + 1
																result.append([u, v, w])
																self.union(parent, rank, x, y)
																
								# Print the contents of result[] to display the built MST
								for u, v, weight in result:
												print("{0}--{1} == {2}".format(u, v, weight))


g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

g.kruskalmst()