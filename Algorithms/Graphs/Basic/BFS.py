class Graph:
    def __init__(self,V):
        self.V=V
        self.adjList={}
        for i in range(self.V):
            self.adjList.update({i:[]})

    def addEdge(self,dest,src):
        self.adjList[dest].append(src)

    def printGraph(self):
        for i in range(len(self.adjList)):
            print(str(i)+'->',end="\t")
            for j in self.adjList[i]:
                print(j,end=" ")
            print()

    def BFS(self,v):
        visited=[False]*self.V
        queue=[]
        queue.append(v)
        visited[v]=True

        while queue:
            s=queue.pop(0)
            print(s)
            for i in self.adjList[s]:
                if visited[i]==False:
                    queue.append(i)
                    visited[i]=True
g=Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(2, 0)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.printGraph()

g.BFS(2)