#Cycle in a Direct Graph
#Similar to DFS + A recstack


class Graph:
				def __init__(self, v):
								self.V = v
								self.adjlist = {}
								for i in range(self.V):
												self.adjlist.update({i: []})
				
				def add_edge(self, dest, src):
								self.adjlist[dest].append(src)
				
				def print_graph(self, graph):
								for v in range(graph.V):
												print("Adjacency List " + str(v) + "\thead", end="")
												for i in graph.adjlist[v]:
																print('->' + str(i), end="")
												print("")
				
				def iscyclicutil(self, graph, v, visited, recstack):
								visited[v] = True
								recstack[v] = True
								for neighbour in graph.adjlist[v]:
												if not visited[neighbour]:
																if self.iscyclicutil(graph, neighbour, visited, recstack):
																				return True
												elif recstack[neighbour]:
																return True
								recstack[v] = False
								return False
				
				def iscyclic(self, graph):
								visited = [False] * graph.V
								recstack = [False] * self.V
								for node in range(self.V):
												if not visited[node]:
																if self.iscyclicutil(graph, node, visited, recstack):
																				return True
								return False


g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
#g.add_edge(2,0)
g.add_edge(2, 3)
#g.add_edge(3,3)
#g.print_graph(g)
if g.iscyclic(g):
				print("Graph is cyclic")
else:
				print("Graph is not cyclic")
