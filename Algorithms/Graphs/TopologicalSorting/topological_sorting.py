"""
Python: Graph Data Structure
        Topological Sorting
        Takes an Extra stack
"""


class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = {}
        
        for i in range(vertices):
            self.adj_list.update({i: []})

    def add_edge(self, dest, src):
        self.adj_list[dest].append(src)

    def topological_sort_util(self, i, visited, stack):
        
        visited[i] = True
        
        for j in self.adj_list[i]:
        
            if not visited[j]:
                self.topological_sort_util(j, visited, stack)
        
        stack.insert(0, i)

    def topological_sort(self):
        
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            
            if not visited[i]:
                
                self.topological_sort_util(i, visited, stack)

        print(stack)


if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(5, 2)
    g.add_edge(5, 0)
    g.add_edge(4, 0)
    g.add_edge(4, 1)
    g.add_edge(2, 3)
    g.add_edge(3, 1)
    g.topological_sort()
