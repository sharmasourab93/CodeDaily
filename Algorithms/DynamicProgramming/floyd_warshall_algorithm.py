"""
Python: Dynamic Programming
								Floyd-Warshall Algorithm
								Complexity: O(n^3)
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
																
																dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
				
				print_solution(dist)
				

# A utility program to print the solution matrix
def print_solution(dist):
				print("Following matrix shows the shortest distances\
											between every pair of vertices")
				
				for i in range(VERTEX):
								print()
								for j in range(VERTEX):
												if dist[i][j] == INF:
																print("%7s"%("INF"), end=" ")
												
												else:
																print("%7d"%(dist[i][j]), end=" ")
												
												if j == VERTEX - 1:
																print(end="")


if __name__ == "__main__":
				graph = [[0, 5, INF, 10],
													[INF, 0, 3, INF],
													[INF, INF, 0, 1],
													[INF, INF, INF, 0]
													]
				floyd_warshall(graph)