"""
Given an array of 6 * 6,

Print max sum of an hour glass
"""
from math import inf


def hour_glass_sum(arr):
    temp, max_,  = [], -inf
    for a in range(0, 4):
        for b in range(0, 4):
            temp = []
            for i in range(a, 3 + a):
                for j in range(b, 3 + b):
                    temp.append(arr[i][j])
            
            temp.pop(3)
            temp.pop(4)
            
            sum_ = sum(temp)
            # print(sum_)
            
            if max_ < sum_:
                max_ = sum_
                
    return max_
    

if __name__ == '__main__':
    arr = """
    0 -4 -6 0 -7 -6
    -1 -2 -6 -8 -3 -1
    -8 -4 -2 -8 -8 -6
    -3 -1 -2 -5 -7 -4
    -3 -5 -3 -6 -6 -6
    -3 -6 0 -8 -6 -7"""
    arr = arr.strip('\n').splitlines()
    arr = [list(map(int, i.strip().split())) for i in arr]
    #print(arr)
    result = hour_glass_sum(arr)
    print(result)
