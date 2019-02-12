"""
Python: Quick Sort
"""


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi-1)
        quick_sort(array, pi+1, high)


def partition(array, low, high):
    pivot = array[high-1]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i + 1


if __name__ == "__main__":
    array = [12, 10, 45, 32, 67, 11, 9]
    quick_sort(array, 0, 7)
    print(array)