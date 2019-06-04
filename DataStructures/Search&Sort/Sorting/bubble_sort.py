"""
Python : Bubble Sort
         Worst Case Performance: O(n^2), O(n^2) Swaps
         Best Case Performance: O(n), O(1) swaps
         Worst Case Space Complexity: O(1) Auxiliary Space
"""


def print_array(array):
    for i in array:
        print(i, end=" ")


def bubble_sort(array, size):
    for i in range(size):
        for j in range(size-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

    print_array(array)


if __name__ == "__main__":
    array = [9, 8, 7, 6, 5, 12]
    bubble_sort(array, len(array))