import sys
class Graph:
    def __init__(self,V):
        self.V=V
        self.adjList={}
        for i in range(self.V):
            l=[sys.maxsize]*self.V
            self.adjList.update({i:[l,object,object,bool]})

    def print_graph(self):
        print("Edge\t Distance")
        for i in range(len(self.adjList)):
            u=self.adjList[i][1]
            wt=self.adjList[i][2]
            print(i,"-",u,"\t",wt)


    def addEdge_Wt(self,src,dest,wt):
        self.adjList[src][0][dest]=wt
        self.adjList[dest][0][src]=wt

    def min_Distance(self):
        for i in range(len(self.adjList)):
            u=


    def Dijkstra(self,src):
        dist=[sys.maxsize]*self.V
        dist[src]=0
        sptSet=[False]*self.V

        for g in range(len(self.adjList)):
            u=self.min_Distance(dist)
            self.adjList[u]
            for v in range
            if self.adjList[u][1]