"""
Python: Divide & Conquer Algorithm
        Median of Two Sorted Array
        Using divide & conquer strategy
Source: Geeksforgeeks
"""


# To Combine and sort array
def combine_array(ar1, ar2):

    ar3 = list(sorted(ar1+ar2))
    return ar3


# To get the median
def get_median(ar1, ar2, n):

    i = 0   # Current index of i/p list ar1[]
    j = 0   # Current index of i/p list ar2[]
    m1, m2 = -1, -1

    # Since there are 2n elements,
    # media will be average of elements at index
    # n-1 and n in the array obtained after merging ar1 and ar2
    count = 0

    while count < n + 1:
        count += 1

        # Below is to handle case where
        # all elements of ar1[] are smaller than smallest
        # (or first) element of ar2[]

        if i == n:
            m1, m2 = m2, ar2[0]
            break

        # Below is to handle case where all
        # elements of ar2[] are smaller than
        # smallest(or first) element of ar1[]
        elif j == n:
            m1, m2 = m2, ar1[0]
            break

        if ar1[i] < ar2[j]:
            m1, m2 = m2, ar2[j]
            i += 1

        else:
            m1, m2 = m2, ar2[j]
            j += 1

    return sum(m1+m2)/2


# Method to find median of the sort-combined array
def find_median(arr):

    # If length of array is even
    if len(arr) % 2 == 0:
        return (arr[int(len(arr)/2)-1]+arr[int(len(arr)/2)])/2

    else:
        return arr[int(len(arr)/2)]


if __name__ == "__main__":
    ar1 = [1, 3, 5, 7]
    ar2 = [2, 4, 6, 8]

    # Median after merging data in Sorted Order
    # {1, 2, 3, 4, 5, 6, 7, 8}
    ar3 = combine_array(ar1, ar2)
    print("The median for the list is: ", find_median(ar3))