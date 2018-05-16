#Graph Creation
class Graph:
    def __init__(self,V):
        self.V=V
        self.adjList={}
        for i in range(V):
            self.adjList.update({i:[]})

    def addEdge(self,dest,src):
        self.adjList[dest].append(src)
        self.adjList[src].append(dest)

    def PrintGraph(self,graph):
        for v in range(graph.V):
            print("Adjacency List "+str(v)+"\thead", end="")
            for i in graph.adjList[v]:
                print('->'+str(i),end="")
            print("")

g=Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(2, 3)
g.addEdge(3, 1)
g.PrintGraph(g)
