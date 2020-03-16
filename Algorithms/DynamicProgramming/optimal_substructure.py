"""
Python: Dynamic Programming (DP)
        Optimal Sub-structure

A given problem has Optimal Substructure property, if
optimal solution of the given problem can be obtained by using
optimal solutions of its sub-problems.

For Example,
The shortest path problem has following optimal substructure property:
If node x lies in the shortest path from a source node u to
destination node v then the shortest path from u to v is combination
of shortest path from u to x and shortest path from x to v.

The standard all pair shortest path algorithms like
Floyd - Warshall  & Bellman - Ford are typical examples of DP.
"""
from copy import deepcopy
from sys import maxsize

# Number of Vertices in the graph
VERTEX = 4
INF = maxsize


def floyd_warshall(graph):
				# Initializing dist to the same value as graph matrix
				dist = deepcopy(graph)
				
				for k in range(VERTEX):
								for i in range(VERTEX):
												for j in range(VERTEX):
																dist[i][j] = min(dist[i][j],
                                 dist[i][k] + dist[k][j])
				
				print_solution(dist)
 

# A utility program to print the solution matrix
def print_solution(dist):
				print("Following matrix shows the shortest distances\
											between every pair of vertices")
				
				for i in range(VERTEX):
								print()
								for j in range(VERTEX):
												if dist[i][j] == INF:
																print("%7s".format("INF"), end=" ")
												
												else:
																print("%7d".format(dist[i][j]), end=" ")
												
												if j == VERTEX - 1:
																print(end="")


if __name__ == "__main__":
				graph = [[0, 5, INF, 10],
													[INF, 0, 3, INF],
													[INF, INF, 0, 1],
													[INF, INF, INF, 0]
													]
				floyd_warshall(graph)