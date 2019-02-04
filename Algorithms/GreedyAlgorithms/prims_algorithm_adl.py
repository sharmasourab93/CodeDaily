"""
Prim's Algorithm for Adjacency List Representation
Using Python's heapq method
1. Create a Min Heap of size V,where V is the number of vertices in the graph
   Every node of min heap contains vertex number & key value of vertex
2. Initialize Min heap with first vertex as root
			The key value assigned to first vertex is 0.
			The key value assigned to all other vertices is INF (infinite)
3. While Min Heap is not empty, do following
			a. Extract the min value node from Min heap. Let the extracted vertex be u
			b. For every adjacent vertex v of u, check if v is in Min Heap.
      If v is in Min Heap and its key value is more than weight of u-v,
      then update the key value of v as weight of u-v.
"""

import sys
import heapq

class Heap:
