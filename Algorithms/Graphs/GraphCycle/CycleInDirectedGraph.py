#Cycle in a Direct Graph
#Similar to DFS + A recStack
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
            print("Adjacency List "+str(v)+"\thead", end="")
            for i in graph.adjList[v]:
                print('->'+str(i), end="")
            print("")
    def isCyclicUtil(self,graph,v,visited,recStack):
        visited[v]=True
        recStack[v]=True
        for neighbour in graph.adjList[v]:
            if visited[neighbour]==False:
                if self.isCyclicUtil(graph,neighbour,visited,recStack)==True:
                    return True
            elif recStack[neighbour]==True:
                return True
        recStack[v]=False
        return False
    
    def isCyclic(self,graph):
        visited=[False]*graph.V
        recStack=[False]*self.V
        for node in range(self.V):
            if visited[node]==False:
                if self.isCyclicUtil(graph,node,visited,recStack)==True:
                    return True
        return False

g=Graph(4)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
#g.addEdge(2,0)
g.addEdge(2,3)
#g.addEdge(3,3)
#g.PrintGraph(g)
if g.isCyclic(g)==True:
    print("Graph is cyclic")
else:
    print("Graph is not cyclic")
