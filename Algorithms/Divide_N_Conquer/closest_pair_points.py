"""
Python: Divide & Conquer Algorithm
        Closest Pair of Points
            i. Naive - Brute Force Approach O(n^2)
           ii. Optimized Approach O( n * log(n))
"""
from sys import maxsize
from math import sqrt


def distance_between(point_a, point_b):
    dist_between = ((point_a[0] - point_b[0]) ** 2) + \
                   ((point_a[1] - point_b[1]) ** 2)

    return sqrt(dist_between)


# Brute Force Approach
# Complexity O(n^2)
def closest_pair_naive(pairs, length):
    min_distance = -maxsize
    closest_pair = ()
    for i in range(len(pairs)):
        for j in range(i+1, len(pairs)):

            point_p, point_q = pairs[i], pairs[j]
            closest_points = distance_between(point_p, point_q)

            if closest_points < min_distance:
                min_distance = closest_points
                closest_pair = (point_p, point_q)

    return closest_pair


if __name__ == "__main__":
    point = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    size = len(point)

    print(" Smallest Distance(Brute Force): ",
          closest_pair_naive(point, size)
          )
