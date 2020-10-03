"""
Python: Dynamic Programming (DP)
        Permutation Coefficient
The coefficient can also be computed recursively
using the below recursive formula:
P(n, k) = P(n-1, k) + k * P(n-1, k-1)
If we observe closely, we can analyze that
the problem has overlapping substructure,
hence we can apply dynamic programming here.
"""


# Leads to Recusion Error for a slightly bigger number
def naive_recursive_permutation(n, k):
    # Base Case
    if n == k:
        return 1
    elif n < k:
        return 0
    
    return naive_recursive_permutation(n-1, k) +\
           k * naive_recursive_permutation(n-1, k-1)


# O(k * k) implementation
def naive_dp_permutatation(n, k):
    # Stored the Calculated Value
    # of Permutation for every i and j
    permute_dict = dict()
    
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            # Base Case
            if j == 0:
                permute_dict[(i, j)] = 1
            # Calculate based on previously
            # stored values
            else:
                permute_dict[(i, j)] = permute_dict[(i-1, j)] + \
                          (j * permute_dict[(i-1, j-1)])
                
            if j < k:
                permute_dict[(i, j+1)] = 0
    
    # print(permute_dict)
    return permute_dict[(n, k)]


# O(n) Implementation
def dp_optimized_permutation(n, k):
    fact = [0 for i in range(n + 1)]
    fact[0] = 1
    
    for i in range(1, n+1):
        fact[i] = i * fact[i-1]
        
    return int(fact[n] / fact[n-k])


if __name__ == '__main__':
    n_, k_ = 10, 3
    # RecursionError
    """
    result_recur = naive_recursive_permutation(n_, k_)
    print("Naive Recursive Permutation of ({0}, {1}) is {2}"
          .format(n_, k_, result_recur))
    """
    result_naive_dp = naive_dp_permutatation(n_, k_)
    print("DP Permutation of ({0}, {1}) is {2}"
          .format(n_, k_, result_naive_dp))
    result_dp = dp_optimized_permutation(n_, k_)
    print("DP Optimized Permutation of ({0}, {1}) is {2}"
          .format(n_, k_, result_dp))
