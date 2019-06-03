"""
Python : Merge Sort
         Worst-case performance: O(n * log n)
         Best-case performance:  O(n * log n) typical, O(n) natural variant
         Average performance:	 O(n * log n)
         Worst-case space complexity: О(n) total with O(n) auxiliary,
                                      O(1) auxiliary with linked lists[1]
"""


def merge_sort(array):

    # print("Splitting :", array)
    if len(array) > 1:

        # Splitting arrays into half
        mid = len(array) // 2
        left, right = array[:mid], array[mid:]

        # Recursively subdividing into left and right
        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        # Comparing elements of left sub-array and Right Sub-array
        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                array[k] = left[i]
                i += 1

            else:
                array[k] = right[j]
                j += 1
            k += 1

        # Iterating through remaining elements of sub-arrays if any
        # Iterating through left sub-array
        while i < len(left):
            array[k] = left[i]
            i += 1
            k += 1

        # Iterating through right sub-array
        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1

    # print("Merging", array)


if __name__ == "__main__":
    array = [10, 54, 1, 89, 13, 12, 98]
    merge_sort(array)
    print(array)