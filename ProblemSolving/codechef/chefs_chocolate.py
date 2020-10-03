""""
Problem Solving: Code Chef
Chef just got a box of chocolates as his birthday gift.
The box contains N chocolates in a row (numbered 1 through N),
where N is even. For each valid i, the i-th chocolate has
    a sweetness value Wi.
Chef wants to eat all the chocolates in the first half of
the box and leave all chocolates in the second half uneaten.
Since he does not like chocolates that are too sweet,
he will be unhappy if at least one of the chocolates he eats
has the maximum sweetness among all the chocolates in the box.

A right cyclic shift by k chocolates (0≤k<N) consists
of moving the last k chocolates in the row to the beginning
in the same order and moving each of the remaining N−k
chocolates k places to the right.
Before eating the first half of the chocolates,
Chef wants to perform some right cyclic shift in such a way
that he will not be unhappy after eating them.
Find the number of ways to do this, i.e.
the number of valid integers k
such that if Chef performs the right cyclic shift by k chocolates
and then eats the first half of the chocolates in the box,
he does not become unhappy.

Input
The first line of the input contains a single integer T
denoting the number of test cases. The description of T test cases follows.
The first line of each test case contains a single integer N.
The second line contains N space-separated integers W1,W2,…,WN.
"""


def shift_n_see(num):
    count = 0
    length = len(num)
    div = length//2
    print(num)
    for i in range(div+1):
        
        if sum(num[:div]) == sum(num[div:]):
            num.insert(0, num.pop())
        elif sum(num[:div]) > sum(num[div:]) or \
             sum(num[:div]) < sum(num[div:]):
            count += 1
    
    return count


if __name__ == '__main__':
    #n = int(input())
    #for i in range(n):
    if True:
        num = ' '.join(input().split())
        num = [int(i) for i in num]
        print(num)
        res = shift_n_see(num)
        print(res)