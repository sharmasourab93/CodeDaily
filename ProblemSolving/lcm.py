"""
Python: Problem Solving
        Lowest Common Multiple or LCM
"""


def lcm(num1, num2):

    greater, lcm = 0, 0

    if num1 > num2:
        greater = num1

    else:
        greater = num2

    while True:

        if greater % num1 == 0 and greater % num2 == 0:
            lcm = greater
            break

        greater += 1

    return lcm


if __name__ == '__main__':
    print(lcm(2, 4))
    print(lcm(2, 8))
    print(lcm(20, 100))



