#Kruskal's MST

class Graph:
    def __init__(self,V):
        self.V=V
        self.graph=[]
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])

    def find(self,parent,i):
        if parent[i]==i:
            return i
        return self.find(parent,parent[i])

    def union(self,parent,rank,x,y):

        xroot=self.find(parent,x)
        yroot=self.find(parent,y)

        if rank[xroot]<ran
