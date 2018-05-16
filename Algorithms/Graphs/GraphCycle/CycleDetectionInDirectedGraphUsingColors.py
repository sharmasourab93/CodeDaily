from enum import Enum

class Color(Enum):
    GRAY=1
    RED=2
    BLACK=3

class Graph:
    def __init__(self,V):
        self.V=V
        self.adjList={}
        for i in range(self.V):
            self.adjList.update({i:[list(),Color(1)]})

    def addEdge(self,src,dest):
            self.adjList[src][0].append(dest)

    def isCyclicUtil(self,i):
        self.adjList[i][1]=Color(2)
        for j in self.adjList[i][0]:
            if self.adjList[j][1].name=='RED': return True
            if self.adjList[j][1].name=='GRAY' and self.isCyclicUtil(j)==True:return True
        self.adjList[i][1]=Color(3)
        return False

    def isCyclic(self):
        for i in range(len(self.adjList)):
            if self.adjList[i][1].name=='GRAY':
                if self.isCyclicUtil(i)==True:
                    return True
        return False


g = Graph(4)
g.addEdge(0, 1)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3,1)
if g.isCyclic():
    print("Graph contains Cycle")
else:
    print("Graph doesn't contain cycles")
