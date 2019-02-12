"""
Python : Selection Sort
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
    selection_sort([9, 8, 7, 6, 5, 12], 6)