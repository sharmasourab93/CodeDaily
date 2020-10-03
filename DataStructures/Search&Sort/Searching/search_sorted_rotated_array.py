"""
Python: Searching Problems In an Array
        An element in a sorted array can be found in
        O(log n) time via binary search.
"""


def pivoted_binary_search(arr, n, key):
    
    pivot = find_pivot(arr, 0, n - 1)
    
    if pivot == -1:
        return search(arr, 0, n-1, key)
    
    
    if arr[pivot] == key:
        return pivot
    
    if arr[0] <= key:
        return search(arr, 0, pivot - 1, key)
    
    return search(arr, pivot + 1, n -1, key)
    
    
def find_pivot(arr, low, high):
    
    if high < low:
        return -1
    
    if high == low:
        return low
    
    mid = int((low + high) / 2)
    
    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1
    
    if arr[low] >= arr[mid]:
        return find_pivot(arr, low, mid-1)
    
    return find_pivot(arr, mid + 1, high)
    
    
def search(arr, key, left, right):
    
    if right < left:
        return -1
    
    mid = int((left + right) / 2)
    
    if arr[mid] == key:
        return mid
    
    elif arr[mid] < key:
        return search(arr, key, mid + 1, right)
    
    else:
        return search(arr, key, left, mid - 1)


if __name__ == '__main__':
    arr = [3, 4, 5, 1, 2]
    key, left, right = 2, 0, len(arr) - 1
    # result = search(arr, key, left, right)
    result = pivoted_binary_search(arr, len(arr), key)
    print(result)
