"""
Python: Dynamic Programming (DP)
        Fibonacci Numbers
        
"""


# Fibonacci Using Dynamic Programming
def fibonacci_dp(n):
    fib_list = [0, 1]
    while len(fib_list) < n + 1:
        fib_list.append(0)
    
    if n <= 1:
        return n
    else:
        if fib_list[n-1] == 0:
            fib_list[n-1] = fibonacci_dp(n-1)
        
        if fib_list[n-2] == 0:
            fib_list[n-2] = fibonacci_dp(n-2)
            
    fib_list[n] = fib_list[n-2] + fib_list[n-1]
    return fib_list[n]
    

if __name__ == '__main__':
    res = fibonacci_dp(9)
    print(res)
