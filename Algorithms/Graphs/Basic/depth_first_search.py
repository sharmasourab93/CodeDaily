"""
Python: Graph Data Structure
        Depth First Search (DFS)
        Worst Case Performance: O(|V| + |E|)

        Depth First Search Can be achieve into two ways:
        1. Recursive Method
        2. Iterative Method
"""


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = {i: [] for i in range(self.V)}

    # Adding edges between Destination & Source Vertex
    def add_edge(self, destination, source):
        self.adj_list[destination].append(source)

    @staticmethod
    def print_graph(graph):
        for v in range(graph.V):
            print("Adjacency List "+str(v)+"\thead", end="")

            for i in graph.adj_list[v]:
                print('->'+str(i), end="")

            print("")

    # A Utility Depth First Search Method
    # Sub-Method of Recursive Type
    def dfs_util(self, visited, index):
        visited[index] = True
        print(index, end=" ")

        for j in range(len(self.adj_list)):
            if not visited[j]:
                self.dfs_util(visited, j)

    # A Primary Depth First Search Algorithm
    # Recursive Type
    def depth_first_search(self, index):
        """
         Depth First Search Algorithm (Recursive)
         1. Index is passed as argument to Utility Method
         2. Visited[Index] = True
         3. Recursively Call Utility Method by \
            iterating over unvisited nodes
        """
        visited = [False] * self.V
        #print("\nDepth First Search:")
        self.dfs_util(visited, index)

    # Depth First Search Iterative
    def dfs_iterative(self, vertex):
        """
        DFS Iterative Algorithm
        1. Iterate over stack
        2. Mark Visited Nodes as True
        3. Append till all nodes are covered
        """
        stack = []
        visited = [False] * self.V

        visited[vertex] = True
        stack.append(vertex)

        while stack:
            holder = stack.pop()
            print(holder, end=" ")

            for i in self.adj_list[holder]:
                if not visited[i]:
                    stack.append(i)
                    visited[i] = True


if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    g.print_graph(g)

    print("\nDFS-Recursive")
    g.depth_first_search(2)
    print("\nDFS-Iterative")
    g.dfs_iterative(2)