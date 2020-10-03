
def min_heapify(array, n, i):
    smallest, l, r = i, (2 * i) + 1, ((2 * i) + 2)
    
    if l < n and array[i] > array[l]:
        smallest = l
    
    if r < n and array[smallest] > array[r]:
        smallest = r
    
    if smallest != i:
        array[smallest], array[i] = array[i], array[smallest]
        
        min_heapify(array, n, smallest)


def build_min_heap(array):
    n = len(array)
    
    for i in range(n//2, -1, -1):
        min_heapify(array, n, i)
        

def extract_k(array, k):
    n = len(array)
    build_min_heap(array)
    print(array)
    for i in range(n-1, n-k-1, -1):
        print("Array in i", array)
        array[i], array[0] = array[0], array[i]
        print("Array after swap", array)
        min_heapify(array, i, 0)
        print("Array in i after min_heapify", array)
        
    
    

if __name__ == '__main__':
    arr = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]
    # print(sorted(arr))
    k = 4
    extract_k(arr, k)
    print(arr)