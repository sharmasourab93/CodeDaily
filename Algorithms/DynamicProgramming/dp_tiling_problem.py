"""
Python: Dynamic Programming (DP)
        Tiling Problem
"""


# Naive Recursive method.
def recursive_tile(n):
    if n == 1 or n == 2:
        return n
    
    return recursive_tile(n - 1) + recursive_tile(n - 2)


def dp_iterative_tile(n):
    
    array = [0] * n
    array[0], array[1] = 1, 2
    
    for i in range(2,  n):
        array[i] = array[i-1] + array[i-2]
    
    return array[n-1]
    
    
if __name__ == '__main__':
    n_ = 4
    result_recur = recursive_tile(n_)
    print("Tiling problem recursive solution for n = {0} is {1}"
          .format(n_, result_recur))
    result_dp = dp_iterative_tile(n_)
    print("Tiling problem DP Iterative solution for n = {0} is {1}"
          .format(n_, result_dp))
