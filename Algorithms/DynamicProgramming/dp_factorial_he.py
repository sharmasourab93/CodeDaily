"""
Python: Dynamic Programming (DP)
        Factorial
    
Given an integer N,
print the factorial of the N (mod 10^9 + 7).

Input:
First line contains one integer, T, number of test cases.
Each test case contains one integer, N.

Output:
For each test case you need to
    print the factorial of N (mod 10^9 + 7).
    
Contraints:
1< T < 10^5
0<= N <= 10^5
"""


MOD = (10**9) + 7


# Recursive Method
def non_dp_factorial_util(number):
    
    if number == 1:
        return 1
    
    return (number * non_dp_factorial_util(number - 1)) % MOD


# Non Dynamic Approach method
# Which leads to Maximum Recursion
def non_dp_factorial(fact_list):
    result_list = []
    for i in fact_list:
        print(non_dp_factorial_util(i))
    
    return result_list


# Dynamic Approach method
def dp_factorial(fact_list, n):
    i, result = 1, 1
    print(result)
    while 0 < i <= n:
        result = (fact_list[i] * result) % ((10**9) + 7)
        print(result)
        i += 1


if __name__ == '__main__':
    list_ = []
    for i in range(20):
        list_.append(i)
    """ Naive Non-DP approach method leads you to
        repeated value calculation which leads to
        RecursionError.
        Hence we trade time complexity with space in the
        dp approach.
    """
    # res = non_dp_factorial(list_)
    # print('\n'.join(res))
    dp_factorial(list_, len(list_)-1)
