"""
Python: Graph Data Structure
        Cycle Detection in an Undirected Graph Using DFS
"""


class Graph:
    
    def __init__(self, v):
        
        self.V = v
        self.adj_list = {i: list() for i in range(self.V)}

    def add_edge(self, src, destination):
        
        self.adj_list[src].append(destination)
        self.adj_list[destination].append(src)

    @staticmethod
    def print_graph(graph):
        
        print("ADL " + "\thead", end="\n")
        for v in range(graph.V):
            print(str(v), end=":\t\t")
            for i in graph.adj_list[v]:
                print('->' + str(i), end="")
        
            print()

    # DFS Utility Method
    def is_cyclic_util(self, v, visited, parent):
        visited[v] = True

        for j in self.adj_list[v]:

            if not visited[j]:
                if self.is_cyclic_util(j, visited, v):
                    return True

            elif parent != j:
                return True

        return False

    # 1. DFS Method
    def is_cyclic_dfs(self):
        visited = [False]*self.V

        for i in self.adj_list:

            if not visited[i]:
                if self.is_cyclic_util(i, visited, -1):
                    return True

        return False


if __name__ == '__main__':
    g = Graph(5)
    g.add_edge(1, 0)
    g.add_edge(1, 2)
    #g.add_edge(2, 4)
    g.add_edge(0, 3)
    g.add_edge(3, 4)
    
    Graph.print_graph(g)
        
    if g.is_cyclic_dfs():
        print("Graph contains cycle.")
    else:
        print("Graph doesn't contain cycle.")
