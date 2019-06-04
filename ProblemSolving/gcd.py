"""
Python: Problem Solving
        Greatest Common Divisor or Highest Common Factor
"""


def gcd_util(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2

    return num1

def gcd(nums):
    if len(nums) == 2:
        return gcd_util(nums[0], nums[1])

    elif len(nums) > 2:
        gcd = gcd_util(nums[0], nums[1])

        for i in range(2, len(nums)):
            gcd = gcd_util(gcd, nums[i])

        return gcd


if __name__ == '__main__':
    gcd_list = [16, 32, 96]
    print(gcd(gcd_list))