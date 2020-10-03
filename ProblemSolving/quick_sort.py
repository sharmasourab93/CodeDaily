

def quick_sort(arr, low, high):
    
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


def partition(arr, low, high):
    
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


if __name__ == '__main__':
    array = [12, 10, 45, 32, 67, 11, 9]
    quick_sort(array, 0, len(array) - 1)
    print(array)
