"""
Heap implementation using Python Module heapq
Heapq: https://docs.python.org/3/library/heapq.html
Source: Geeksforgeeks, self
"""
from heapq import heappush, heappop, heapify
from math import ceil


class MinHeap:
				"""A Min Heap Class"""
				
				def __init__(self):
								self.heap = []
				
				# Returns parent index
				def parent(self, i):
								return ceil((i-1)/2)
				
				# Method to insert elements into the heap
				def insert_key(self, k):
								heappush(self.heap, k)
				
				# To decrease key and replace the element in the heap
				def decrease_key(self, i, new_val):
								self.heap[i] = new_val
								while self.heap[self.parent(i)] > self.heap[i] and i != 0:
												self.heap[i], self.heap[self.parent(i)] = \
																self.heap[self.parent(i)], self.heap[i]
				
				# Remove the top most element in the heap
				def extract_min(self):
								return heappop(self.heap)
				
				# Delete a key from the heap
				def delete_key(self, i):
								self.decrease_key(i, float("-inf"))
								self.extract_min()
								
				# Return minimum element from the heap
				def get_min(self):
								return self.heap[0]

				
if __name__ == "__main__":
				heap_object = MinHeap()
				heap_object.insert_key(3)
				heap_object.insert_key(2)
				heap_object.delete_key(1)
				heap_object.insert_key(15)
				heap_object.insert_key(5)
				heap_object.insert_key(4)
				heap_object.insert_key(45)
				print("Minimum Value Extracted ", heap_object.extract_min())
				print("Getting Min Value ", heap_object.get_min())
				heap_object.decrease_key(2, 1)
				print("Decreasing Key \nGetting Min Value ", heap_object.get_min())
				print(heap_object.get_min())