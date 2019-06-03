"""
Python: Quick Sort
        Worst-case performance:	O(n^2)
        Best-case performance:	O(n log n) (simple partition)
        Average performance:	O(n log n)
        Worst-case space complexity: O(n) auxiliary (naive), O(log n) auxiliary
"""


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi-1)
        quick_sort(array, pi+1, high)


def partition(array, low, high):
    pivot = array[high]
    i = low-1

    for j in range(low, high):

        # If current element is
        # smaller than or equal to pivot
        if array[j] <= pivot:

            # increment index of smaller element
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i+1], array[high] = array[high], array[i+1]

    return i+1


if __name__ == "__main__":
    array = [12, 10, 45, 32, 67, 11, 9]
    quick_sort(array, 0, len(array)-1)
    print(array)