"""
Python: Graph Data Structure
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
				
				# To Add an edge between
				# a source u and a destination v
				def add_edge(self, u, v):
								self.graph[u].append(v)
				
				# To Find Parent node
				def find_parent(self, parent, i):
								if parent[i] == -1:
												return i
								
								if parent[i] != -1:
												return self.find_parent(parent, parent[i])
				
				# To Find the Union
				def union(self, parent, x, y):
								x_set = self.find_parent(parent, x)
								y_set = self.find_parent(parent, y)
								parent[x_set] = y_set
				
				# To Find if the graph is cyclic
				def is_cyclic(self):
								parent = [-1] * self.V
								
								for i in self.graph:
												for j in self.graph[i]:
																x = self.find_parent(parent, i)
																y = self.find_parent(parent, j)
																if x == y:
																				return True
																self.union(parent, x, y)


if __name__ == '__main__':
				g = Graph(3)
				g.add_edge(0, 1)
				g.add_edge(1, 2)
				g.add_edge(2, 0)
				
				if g.is_cyclic():
								print("Graph is cyclic")
				else:
								print("No Cycle in graph")