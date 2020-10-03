"""
Python: Array Rotation
        On Being Given an array, rotate the array by k elements.
"""


def rotate_ok(array, k):
    
    temp = []
    
    for i in range(0, k):
        temp.append(array[i])
        
    for i in temp:
        array.remove(i)
    
    return array + temp



    


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6]
    k = 2
    result = rotate_ok(arr, k)
    print(result)
