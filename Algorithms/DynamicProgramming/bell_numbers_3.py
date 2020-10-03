"""
Python: Dynamic Programming (DP)
        Bell Numbers
        Let S(n, k) be total number of partitions of n elements
        into k sets. The value of nth bell number is
        Sum of S(n, k) for k=1 to n.


"""


def simple_bell_method(N):
    if N == 0:
        print(1)
    if N > 1:
    
    
