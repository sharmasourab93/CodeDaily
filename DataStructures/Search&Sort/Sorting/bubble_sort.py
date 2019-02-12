"""
Python : Bubble Sort
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
    bubble_sort([9, 8, 7, 6, 5, 12], 6)