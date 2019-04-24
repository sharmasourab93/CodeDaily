"""
Python: Divide & Conquer Algorithm
        Binary Search Algorithm

        Worst complexity: O(log n)
        Average complexity: O(log n)
        Best complexity: O(1)

        Space complexity: O(1)

        Data structure: Array

        Cons : Works with Sorted arrays
"""
from math import ceil


def binary_search(array, low, high, target):
    if low < high:

        m = low + ceil((high - low) / 2)

        if array[m] == target:
            return m

        elif array[m] > target:
            return binary_search(array, low, m-1, target)

        else:
            return binary_search(array, m, high, target)

    else:
        return -1


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    bin_search = binary_search(array, 0, len(array)-1, 10)
    print("Index: ", bin_search)