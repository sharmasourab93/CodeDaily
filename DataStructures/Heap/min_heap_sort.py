"""
Python: Min Heap Implementation
"""


def min_heapify(array, n, i):
    
    smallest, l, r = i, (2 * i) + 1, (2 * i) + 2
    
    if l < n and array[i] > array[l]:
        smallest = l
        
    if r < n and array[smallest] > array[r]:
        smallest = r
        
    if smallest != i:
        array[smallest], array[i] = array[i], array[smallest]
        min_heapify(array, n, smallest)


def build_min_heap(array):
    n = len(array)
    
    for i in range(0, n//2+1):
        min_heapify(array, n, i)


def min_heap_sort(array):
    n = len(array)
    build_min_heap(array)
    # print("Array After Building Min Heap", array)
    for i in range(n-1, -1, -1):
        array[i], array[0] = array[0], array[i]
        
        min_heapify(array, i, 0)
    


if __name__ == '__main__':
    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    print("Given array is:", arr)
    min_heap_sort(arr)
    k = 4
    print("Min Heap is sorted in:", end=" ")
    print(" ".join(list(map(str, arr))))
    print("K'th Smallest array", arr[-k])