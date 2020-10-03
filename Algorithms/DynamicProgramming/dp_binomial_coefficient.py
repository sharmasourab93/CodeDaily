"""
Python: Dynamic Programming (DP)
        Binomial Coefficient
"""


# Simple Recursive Binomial Coefficient
def binomial_coefficient(n, k):
    
    if k == 0 or k == n:
        return 1
    
    return (binomial_coefficient(n-1, k-1) +
            binomial_coefficient(n-1, k))


def dp_binomial_coefficient(n, k):
    """
    Since Binomial Coefficient deals with
    overlapping Subproblem,
    this problem can be solved at a lesser
    time complexity using Dynamic Programming
    Time Complexity: O(n * k)
    Aux Space: Dictionary key (n, k) for each iteration +
               Pertaining value for every key
    """
    store_dict = dict()
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                store_dict.update({(i, j): 1})
            else:
                key = (i, j)
                value = (store_dict[(i-1, j-1)] +
                         store_dict[(i-1, j)])
                store_dict.update({key: value})
    
    # print(store_dict)
    return store_dict[(n, k)]


if __name__ == '__main__':
    print("Using Simple Recusive Method")
    num, k_ = 100, 2
    result = binomial_coefficient(num, k_)
    print("Value of C({0}, {1}) is {2}".format(num, k_, result))
    
    print("\nUsing Dynamic Programmng Approach")
    result = dp_binomial_coefficient(num, k_)
    print("Value of C({0}, {1}) is {2}".format(num, k_, result))
