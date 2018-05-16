'''
Given an array of n integers. Initially, all elements are zero. You are asked to complete q queries of two kinds:

1 x y l r: for each i in range [x, y] flip the l-th bit to r-bit of i-th element.

2 x y: check if x-th element equals y-th element.

Input Format

The first line contains an integer T denoting the number of test cases. Each test case is described as follow:

A line contains two space-separated integers n, q denoting the size of array and the number of queries. q queries follow are described as in the statement.

Output Format

For each query of kind 2, output a single line contains "YES" if two numbers are equal, otherwise "NO".

Constraints

1 ≤ T ≤ 100
1 ≤ n ≤ 105
1 ≤ q ≤ 105
1 ≤ sum of n over all test cases ≤ 2.105
1 ≤ sum of q over all test cases ≤ 2.105
1 ≤ x ≤ y ≤ n
0 ≤ l ≤ r ≤ 109

EXPLANATION
The initial array is [0, 0].

Query 1: 1 1 1 5 6, the array becomes [96, 0]. Note that 96 = 25 + 26.

Query 2: 2 1 2, output "NO".

Query 3: 1 2 2 5 6, the array becomes [96, 96].

Query 4: 2 1 2, output "YES".
'''
T=int(input())
n=int(input())
q=int(input())
