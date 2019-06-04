"""
Python : Selection Sort
         Worst-case performance: О(n^2) comparisons, О(n) swaps
         Best-case performance:	 О(n^2) comparisons, О(n) swaps
         Average performance:	 О(n^2) comparisons, О(n) swaps
         Worst-case space complexity:	O(1) auxiliary
"""


def print_array(array):
    for i in array:
        print(i, end=" ")


def selection_sort(array, size):
    for i in range(size):
        minimum = i

        for j in range(size):
            if array[minimum] > array[j]:
                minimum = j

        array[i], array[minimum] = array[minimum], array[i]

    print_array(array)


if __name__ == "__main__":
    array = [9, 8, 7, 6, 5, 12]
    selection_sort(array, len(array))