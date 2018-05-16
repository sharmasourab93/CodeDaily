class Graph:
    def __init__(self,V):
        self.V=V
        self.adjList={}
        for i in range(V):
            self.adjList.update({i:[]})

    def addEdge(self,dest,src):
        self.adjList[dest].append(src)

    def PrintGraph(self,graph):
        for v in range(graph.V):
            print("Adjacency List "+str(v)+"\thead",end="")
            for i in graph.adjList[v]:
                print('->'+str(i),end="")
            print("")

    def DFSUtil(self,visited,index):
        visited[index]=True
        print(index)
        for j in range(len(self.adjList)):
            if not visited[j]:
                self.DFSUtil(visited,j)

    def DFS(self,index):
        visited=[False]*self.V
        self.DFSUtil(visited,index)


g=Graph(4)
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
g.PrintGraph(g)

g.DFS(2)