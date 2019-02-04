#Prim's MST
import sys


class Graph:
				def __init__(self, v):
								self.V = v
								self.graph = [[0 for column in range(V)] for row in range(V)]
				
				def print_mst(self, parent):
								print("Edge\t Weight")
								for i in range(1, self.V):
												print(parent[i], "-", i, "\t", self.graph[i][parent[i]])
				
				def min_key(self, key, mstset):
								min, min_index = sys.maxsize, 0
								for v in range(self.V):
												if key[v] < min and mstset[v]:
																min = key[v]
																min_index = v
								return min_index
				
				def prim_mst(self):
								key = [sys.maxsize]*self.V
								parent = [None]*self.V
								key[0] = 0
								mstset = [False]*self.V
								
								parent[0] = -1
								
								for cout in range(self.V):
												u = self.min_key(key, mstset)
												mstset[u] = True
												
												for v in range(self.V):
																if 0 < self.graph[u][v] < key[v] and mstset[v]:
																				key[v] = self.graph[u][v]
																				parent[v] = u
								
								self.print_mst(parent)


g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
											[2, 0, 3, 8, 5],
											[0, 3, 0, 0, 7],
											[6, 8, 0, 0, 9],
											[0, 5, 7, 9, 0],
											]
g.prim_mst()
