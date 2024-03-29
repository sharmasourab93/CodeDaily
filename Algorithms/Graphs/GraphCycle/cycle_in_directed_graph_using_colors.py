"""
Python: Graph Data Structure
        Cycle Detection In a Graph Using Colors
"""
from enum import Enum


class Color(Enum):
    GRAY = 1
    RED = 2
    BLACK = 3


class Graph:
    
    def __init__(self, V):
        
        self.V = V
        self.adj_list = {i: [list(), Color.GRAY] for i in range(self.V)}

    def add_edge(self, src, dest):
        
        self.adj_list[src][0].append(dest)

    @staticmethod
    def print_graph(graph):
        
        print("ADL " + "\thead", end="\n")
        for v in range(graph.V):
            print(str(v), end=":\t\t")
            for i in graph.adj_list[v]:
                print('->' + str(i), end="")
        
            print()

    def is_cyclic_util(self, i):
        
        self.adj_list[i][1] = Color.RED

        for j in self.adj_list[i][0]:
            if self.adj_list[j][1].name == 'RED':
                return True

            if self.adj_list[j][1].name == 'GRAY' and \
                    self.is_cyclic_util(j):
                return True
        
        self.adj_list[i][1] = Color.BLACK
        return False

    def is_cyclic(self):
        for i in range(len(self.adj_list)):

            if self.adj_list[i][1].name == 'GRAY':
                if self.is_cyclic_util(i):
                    return True

        return False


if __name__ == '__main__':
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    Graph.print_graph(g)
    
    if g.is_cyclic():
        print("Graph contains Cycle")
    else:
        print("Graph doesn't contain cycles")
