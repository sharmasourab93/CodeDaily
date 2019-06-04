"""
Python : Heap Sort
         Worst-case performance: O(n * log n)
         Best-case performance:  O(n * log n)
         Average performance:    O(n * log n)
         Worst-case space complexity: O(n), total O(1) auxiliary
"""


def print_array(array):
    for i in array:
        print(i, end=" ")
        
        
def heapify(array, size, i):
    largest = i
    left, right = 2 * i + 1, 2 * i + 2

    if left < size and array[left] > array[i]:
        largest = left

    if right < size and array[right] > array[largest]:
        largest = right

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, size, largest)


def heap_sort(array, size):

    for i in range(size, -1, -1):
        heapify(array, size, i)

    for i in range(size-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)

    print_array(array)


if __name__ == "__main__":
    array = [9, 8, 7, 6, 5, 12]
    heap_sort(array, len(array))