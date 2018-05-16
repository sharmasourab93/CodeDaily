#Topological Sorting
class Graph:
    def __init__(self,V):
        self.V=V
        self.adjList={}
        for i in range(V):
            self.adjList.update({i:[]})

    def addEdge(self,dest,src):
        self.adjList[dest].append(src)

    def topologicalSortUtil(self,i,visited,stack):
        visited[i]=True
        for j in self.adjList[i]:
            if visited[j]==False:
                self.topologicalSortUtil(j,visited,stack)
        stack.insert(0,i)

    def topologicalSort(self):
        visited=[False]*self.V
        stack=[]

        for i in range(self.V):
            if visited[i]==False:
                self.topologicalSortUtil(i,visited,stack)

        print(stack)

g=Graph(6)
g.addEdge(5,2)
g.addEdge(5,0)
g.addEdge(4,0)
g.addEdge(4,1)
g.addEdge(2,3)
g.addEdge(3,1)
g.topologicalSort()
