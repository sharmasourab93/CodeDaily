"""
Python: Graph Data Structure
        Check if a given graph is Bipartite?
"""


class Graph:
    
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(self.V)]
                      for _ in range(self.V)]
        self.color_array = [-1 for _ in range(self.V)]
    
    def is_bipartite_util(self, src):
        
        queue = list()
        queue.append(src)
        
        while queue:
            
            u = queue.pop()
            
            if self.graph[u][u] == 1:
                return False
            
            for v in range(self.V):
                
                if self.graph[u][v] == 1 and self.color_array[v] == -1:
                
                    self.color_array[v] = 1 - self.color_array[u]
                    queue.append(v)
                    
                elif self.graph[u][v] == 1 and self.color_array[v] == self.color_array[u]:
                    return False
                
            return True
    
    def is_bipartite(self):
        """
        Following is a simple algorithm to find out
        whether a given graph is Bipartite or not use BFS.
        
        1. Assign RED color to the source vertex (putting into set U)
        2. Color all the neighbors with Blue Color (putting into set V)
        3. Color all neighbor's neighbor with RED (putting into SET U)
        4. Assign Color to all vertices such that it satisfies
            all the contraints of m way coloring problem where m = 2.
        5. While assigning colors, if we find a neighbor
            which is colored as current vertex, then the graph
            cannot be colored with 2 vertices (graph is not Bipartite)
        :return: True or False
        """
        
        for i in range(self.V):
            if self.color_array[i] == -1:
                if not self.is_bipartite_util(i):
                    return False
                
        return True
    

if __name__ == '__main__':
    graph = Graph(4)
    
    graph.graph = [[0, 1, 0, 1],
                   [1, 0, 1, 0],
                   [0, 1, 0, 1],
                   [1, 0, 1, 0]
                   ]
    print("Yes" if graph.is_bipartite() else "No")
