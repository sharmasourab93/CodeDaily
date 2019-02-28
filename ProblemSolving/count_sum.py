"""
Python: Problem solving
        Count n pairs
"""
from math import floor


def count_sum_pairs(array, k):
    array.sort()
    count = 0
    n = len(array)
    i, j = 0, n - 1
    while i <= floor(n / 2) < j:
        if k - (array[i] + array[j]) == 0:
            count += 1
            print(array[i], print(array[j]))
            i += 1
            j -= 1

        elif k - (array[i] + array[j]) > 0:
            i += 1

        else:
            j -= 1

    return count


print("Count for [0,0] with 0 as k", count_sum_pairs([0, 0], 0))
print("Count for [1,2,3,4,5] for k as 6", count_sum_pairs([5, 4, 3, 2, 1], 6))
print("Count for [2, 6,3,3,4] with k as 6", count_sum_pairs([2, 4, 3, 3, 6], 6))