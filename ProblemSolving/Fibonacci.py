#Naive Fibonacci Approach
def fib(n):
    if n==0: return 0
    if n==1: return 1
    return fib(n-1)+fib(n-2)

def fibNth(n,lookup):
    if n<=1: lookup[n]=n
    else:
        lookup[n]=fibNth(n-1,lookup)+fibNth(n-2,lookup)
    return lookup[n]
n=9
lookup=[-1]*(n+1)
print(fib(n))
print(fibNth(n,lookup))
print(lookup)