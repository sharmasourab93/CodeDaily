"""
Python: Insertion Sort
"""


def print_array(array):
    for i in array:
        print(i, end=" ")


def insertion_sort(array, size):
    for i in range(1, size):
        key = array[i]
        j = i-1

        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key

    print_array(array)


if __name__ == "__main__":
    insertion_sort([9, 8, 7, 6, 5, 12], 6)