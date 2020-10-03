"""
Python: Max Heap Implementation
"""


def max_heapify(array, n, i):
    
    largest, l, r = i, (2 * i) + 1, ((2 * i) + 2)
    
    if l < n and array[i] < array[l]:
        largest = l
        
    if r < n and array[largest] < array[r]:
        largest = r
    
    if largest != i:
        array[largest], array[i] = array[i], array[largest]
        
        max_heapify(array, n, largest)
        

def build_max_heap(array):
    n = len(array)
    
    for i in range((n//2)-1, -1, -1):
        max_heapify(array, n, i)
        

def max_heap_sort(array):
    n = len(array)
    build_max_heap(array)
    print("Array After Building Max Heap", array)
    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        max_heapify(array, i, 0)
        

if __name__ == '__main__':
    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print("Given array is:", arr)
    max_heap_sort(arr)
    print("Max Heap is sorted in:", end=" ")
    print(" ".join(list(map(str, arr))))
