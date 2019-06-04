"""
Python: Graph Data Structure
        Breadth First Search (BFS)
        Worst Case Performance: O(|V| + |E|)
"""


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = {i: [] for i in range(self.V)}

    # Adds an edge between a source node & destination node
    def add_edge(self, destination, source):
        self.adj_list[destination].append(source)

    # Prints the Graph
    def print_graph(self):
        for i in range(len(self.adj_list)):
            print("\n" + str(i) + '->', end="\t")

            for j in self.adj_list[i]:
                print(j, end=" ")

    # Breadth First Search Algorithm
    def breadth_first_search(self, vertex):
        """ BFS Works On Queue data structure """

        visited = [False] * self.V
        queue = list()
        # Appending the vertex to an empty queue
        queue.append(vertex)

        # Marking the Visiting Vertex as True
        visited[vertex] = True
        print("\n\nBreadth First Search: ", end=" ")
        while queue:
            # Popping the First Element in queue
            s = queue.pop(0)
            print(s, end=" ")

            # Visiting the adjacent vertices of queue
            # And Validating if the vertex is visited
            for i in self.adj_list[s]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True


if __name__ == '__main__':
    g = Graph(4)
    """
        0  ---> 1
        ^      /^
        |    /  |
        |  /    |
        2  ---> 3
    """
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 0)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 1)

    g.print_graph()

    g.breadth_first_search(2)
