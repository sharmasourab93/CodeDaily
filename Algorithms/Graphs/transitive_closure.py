"""
Python: Graph Data Structure
		Find a Transitive Closure
"""
from collections import defaultdict


class Graph:
				def __init__(self, vertices):
								self.V = vertices
								self.tc = [[0] * self.V] * self.V
								self.adj_list = defaultdict(list)
				
				# To Add an edge between a source & destination
				def add_edge(self, source, destination):
								self.adj_list[source].append(destination)
				
				# A Utility DFS method to visit all nodes
				def dfs_util(self, s, v):
								self.tc[s][v] = 1
								
								for i in self.adj_list[v]:
												if self.tc[s][i] == 0:
																self.dfs_util(s, i)
				
				# A method to find the Transitive Closure
				def transitive_closure(self):
								for i in range(self.V):
												self.dfs_util(i, i)
												
								print(self.tc)


if __name__ == '__main__':
				g = Graph(4)
				g.add_edge(0, 1)
				g.add_edge(0, 2)
				g.add_edge(1, 2)
				g.add_edge(2, 0)
				g.add_edge(2, 3)
				g.add_edge(3, 3)
				
				g.transitive_closure()