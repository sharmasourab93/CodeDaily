"""
Python: Dynamic Programming (DP)

Let's look at a sample problem:
Let us say that you are given a number N,
you've to find the number of different ways to write
it as the sum of 1, 3 and 4.
"""


def counting_prob(sum_set, given_n):
    dp_list = [0] * given_n
    dp_list[0], dp_list[1], dp_list[2] = 1, 1, 1
    dp_list[3] = 2


if __name__ == '__main__':
    set_, n = {1, 3, 4}, 5
    res = counting_prob(set_, n)
    print(res)
