#Transitive Closure of a graph
from collections import defaultdict
class Graph:
    def __init__(self,V):
        self.V=V
        self.tc=[[0 for j in range(self.V)]for i in range(self.V)]
        self.adjList=defaultdict(list)

    def addEdge(self,src,dest):
        self.adjList[src].append(dest)


    def DFSUtil(self,s,v):
        self.tc[s][v]=1
        for i in self.adjList[v]:
            if self.tc[s][i]==0:
                self.DFSUtil(s,i)

    def transitiveClosure(self):
        for i in range(self.V):
            self.DFSUtil(i,i)
        print(self.tc)

g=Graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)
g.addEdge(3,3)

g.transitiveClosure()
