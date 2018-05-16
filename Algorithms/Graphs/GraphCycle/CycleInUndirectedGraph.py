# Cycle Detection in a Graph
# Using DFS and UnionFind
class Graph:
    def __init__(self,V):
        self.V=V
        self.adjList={}
        for i in range(self.V):
            self.adjList.update({i:list()})
    def addEdge(self,src,dest):
        self.adjList[src].append(dest)

#Using DFS
    def isCyclicUtil(self,v,visited,parent):
        visited[v]=True
        for j in self.adjList[v]:
            if not visited[j]:
                if self.isCyclicUtil(j,visited,v):
                    return True
            elif parent!=-1:
                return True
        return False

    def isCyclicDFS(self):
        visited=[False]*self.V
        for i in self.adjList:
            if not visited[i]:
                if self.isCyclicUtil(i,visited,-1):
                    return True
        return False

#Below is using Union Find method
    def find_parent(self,i,parent):
        if parent[i]==-1:
            return i
        if parent[i]!=-1:
            return self.find_parent(parent[i],parent)
    def union(self,parent,x,y):
        x_set=self.find_parent(x,parent)
        y_set=self.find_parent(y,parent)
        parent[x_set]=y_set

    def isCyclicUnionFind(self):
        parent=[-1]*self.V
        for i in self.adjList:
            for j in self.adjList[i]:
                x=self.find_parent(i,parent)
                y=self.find_parent(j,parent)
                if x==y:
                    return True
                self.union(parent,x,y)

g=Graph(5)
g.addEdge(1,0)
g.addEdge(1,2)
g.addEdge(2,1)
g.addEdge(0,3)
g.addEdge(3,4)

'''if g.isCyclicUnionFind():
    print("Graph contains cycle.")
else:
    print("Graph doesn't contain cycle.")'''

if g.isCyclicDFS():
    print("Graph contains cycle.")
else:
    print("Graph doesn't contain cycle.")
