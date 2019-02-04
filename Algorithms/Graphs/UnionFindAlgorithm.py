"""
Union Find Algorithm
Find: Determine which subset a particular element is in
						Can be used to determine if 2 elements are in the same subset
Union: Join two subsets into a single subset
Union find algorithm can be used for finding cycle in an undirected graph
"""
from collections import defaultdict


class Graph:
				
				def __init__(self, vertices):
								self.V = vertices
								self.graph = defaultdict(list)
				
				def add_edge(self, u, v):
								self.graph[u].append(v)
								
				def find_parent(self, parent, i):
								if parent[i] == -1:
												return i
								
								if parent[i] != -1:
												return self.find_parent(parent, parent[i])
								
				def union(self, parent, x, y):
								x_set = self.find_parent(parent, x)
								y_set = self.find_parent(parent, y)
								parent[x_set] = y_set
								
				def iscyclic(self):
								parent = [-1] * self.V
								
								for i in self.graph:
												for j in self.graph[i]:
																x = self.find_parent(parent, i)
																y = self.find_parent(parent, j)
																if x == y:
																				return True
																self.union(parent, x, y)


g = Graph(3)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 0)

if g.iscyclic():
				print("Graph is cyclic")
else:
				print("No Cycle in graph")