# Cycle Detection in a Graph
# Using DFS and UnionFind


class Graph:
				def __init__(self, v):
								self.V = v
								self.adjlist = {}
								for i in range(self.V):
												self.adjlist.update({i: list()})
				
				def add_edge(self, src, dest):
								self.adjlist[src].append(dest)
				
				#Using DFS
				def iscyclicutil(self, v, visited, parent):
								visited[v] = True
								for j in self.adjlist[v]:
												if not visited[j]:
																if self.iscyclicutil(j, visited, v):
																				return True
												elif parent != -1:
																return True
								return False
				
				def is_cyclic_dfs(self):
								visited = [False]*self.V
								for i in self.adjlist:
												if not visited[i]:
																if self.iscyclicutil(i, visited, -1):
																				return True
								return False
				
				#Below is using Union Find method
				def find_parent(self, i, parent):
								if parent[i] == -1:
												return i
								if parent[i] != -1:
												return self.find_parent(parent[i], parent)
				
				def union(self, parent, x, y):
								x_set = self.find_parent(x, parent)
								y_set = self.find_parent(y, parent)
								parent[x_set] = y_set
				
				def iscyclic_unionfind(self):
								parent = [-1]*self.V
								for i in self.adjlist:
												for j in self.adjlist[i]:
																x = self.find_parent(i, parent)
																y = self.find_parent(j, parent)
																if x == y:
																				return True
																self.union(parent, x, y)


g = Graph(5)
g.add_edge(1, 0)
g.add_edge(1, 2)
g.add_edge(2, 1)
g.add_edge(0, 3)
g.add_edge(3, 4)

'''if g.iscyclic_unionfind():
    print("Graph contains cycle.")
else:
    print("Graph doesn't contain cycle.")'''

if g.is_cyclic_dfs():
				print("Graph contains cycle.")
else:
				print("Graph doesn't contain cycle.")
