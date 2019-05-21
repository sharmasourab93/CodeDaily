"""
Python: Divide & Conquer Algorithm
        Merge Sort

        Best Case: O(n * log n )
        Average Case: O(n * log n )
        Worst Case: O(n * log n)

        Memory: n

        Stable: Yes

        Method: Merging
"""
from math import floor


def merge(array, low, mid, high):

    n1 = mid - low + 1
    n2 = high - mid

    r1 = []
    r2 = []

    i, j = 0, 0

    for i in range(n1):
        r1.append(array[low+i])

    for j in range(n2):
        r2.append(array[mid-1+j])

    i, j, k = 0, 0, low

    while i < n1 and j < n2:

        if r1[i] <= r2[j]:
            array[k] = r1[i]
            i += 1
        else:
            array[k] = r2[j]
            j += 1

        k += 1

        while i < n1:
            array[k] = r1[i]
            i += 1
            k += 1

        while j < n2:
            array[k] = r2[j]
            j += 1
            k += 1


def merge_sort(array, low, high):
    if low < high:
        mid = floor((low + high) / 2)
        merge_sort(array, low, mid)
        merge_sort(array, mid+1, high)
        merge(array, low, mid, high)


if __name__ == "__main__":
    array = [10, 54, 1, 89, 13, 12, 98]
    merge_sort(array, 0, 7)
    print(array)