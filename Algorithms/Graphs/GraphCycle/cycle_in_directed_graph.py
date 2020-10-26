"""
Python: Graph Data Structure
        Cycle Detection In A Directed Graph
        Similar to DFS + A rec_stack

"""


class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = {i: [] for i in range(self.V)}

    # To add an edge between a destination and source node
    def add_edge(self, destination, source):
        self.adj_list[destination].append(source)

    @staticmethod
    def print_graph(graph):
        print("ADL " + "\thead", end="\n")
        for v in range(graph.V):
            print(str(v), end=":\t\t")
            for i in graph.adj_list[v]:
                print('->' + str(i), end="")

            print()

    # A Utility Recursive Cycle Detection Method
    def is_cyclic_util(self, visited, rec_stack, v):
        visited[v] = True
        rec_stack[v] = True

        for neighbour in self.adj_list[v]:

            if not visited[neighbour]:
                if self.is_cyclic_util(visited, rec_stack, neighbour):
                    return True

            elif rec_stack[neighbour]:
                return True

        rec_stack[v] = False
        return False

    # A Driver Method to Detect Cycle
    def is_cyclic(self, graph):
        visited = [False] * graph.V
        rec_stack = [False] * self.V

        for node in range(self.V):
            if not visited[node]:

                if self.is_cyclic_util(visited, rec_stack, node):
                    return True

        return False


if __name__ == "__main__":
    g = Graph(4)

    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    # g.add_edge(2, 0)
    g.add_edge(2, 3)

    g.print_graph(g)

    if g.is_cyclic(g):
        print("Graph is cyclic")
    else:
        print("Graph is not cyclic")
