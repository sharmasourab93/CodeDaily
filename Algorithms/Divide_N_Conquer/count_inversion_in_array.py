"""
Python: Divide & Conquer Algorithm
        Count Inversion In An Array
         i. Naive Solution - O(n^2)
        ii. Using Enhanced Merge Sort - O(n * log n)

"""


def merge(arr, temp, left, mid, right):

    inv_count = 0
    i, j, k = left, mid, left

    while i <= mid - 1 and j <= right:

        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
            k += 1

        else:
            temp[k] = arr[j]
            k += 1
            j += 1
            inv_count = inv_count+(mid-i)

    while i <= mid-1:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    for i in range(left, right):
        arr[i] = temp[i]

    return inv_count


# Merge Sort Driver Function
def merge_sort_driver(arr, temp, left, right):

    inv_count = 0

    if right > left:
        mid = (right+left)/2
        inv_count = merge_sort_driver(arr, temp, left, mid)
        inv_count += merge_sort_driver(arr, temp, mid+1, right)
        inv_count += merge(arr, temp, mid+1, right)

    return inv_count


# Primary Merge Sort Function
# O(n log n) Solution
def merge_sort(arr, arr_size):
    temp = [] * (arr_size-1)
    return merge_sort_driver(arr, temp, 0, arr_size-1)


# Naive method to get
# Inversion Count of the array
# O(n^2) Solution
def get_inversion_count(arr, n):
    inv_count = 0

    for i in range(n):
        for j in range(i+1, n):

            if arr[i] > arr[j]:
                inv_count += 1

    return inv_count


if __name__ == "__main__":
    arr = [1, 20, 6, 4, 5]

    inversion_counter = get_inversion_count(arr, len(arr))
    merge_counter = merge_sort(arr, len(arr)-1)

    print("Using Naive Inversion Method: ", inversion_counter)
    print("Using Enhanced Merge Sort Method: ", merge_counter)