"""
Python: Divide & Conquer Algorithm
        Finding Power using Divide & Conquer Strategy
        The Following code has two methods:
         i. Naive Approach For Finding Power - O(n)
        ii. Optimized Approach For Finding Power - O(log n)
"""


# Naive Approach
# Complexity O(n)
def power(x, y):

    if y == 0:
        return 1

    # Recursively calling the power method and
    # calculating the same value twice.
    elif y % 2 == 0:
        return power(x, int(y/2)) * power(x, int(y/2))

    else:
        return x * power(x, int(y/2)) * power(x, int(y/2))


# Optimized Approach
# Complexity O(log n)
def optimized_power(x, y):
    if y == 0:
        return 1

    # Storing the calculated value and
    # Hence preventing calculation of values more than once.
    temp = optimized_power(x, y/2)

    if y % 2 == 0:
        return temp * temp

    else:
        return x * temp * temp


if __name__ == "__main__":

    x, y = 3, 3
    print("Naive: ", power(x, y))
    print("Optimized: ", power(x, y))