""""
Python: Dynamic Programming (DP)
        Ugly Numbers:
        Ugly numbers are numbers whose only
        prime factors are 2, 3 or 5.
        The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, …
        shows the first 11 ugly numbers.
        By convention, 1 is included.

Given a number n, the task is to find n’th Ugly number.
Examples:
1)Input  : n = 7;   Output : 8
2)Input  : n = 10;   Output : 12
3)Input  : n = 15;   Output : 24
4)Input  : n = 150;  Output : 5832

"""


# Dynamic Programming Solution
def ugly_numbers(num):
    prime_fac_list = [0] * num
    prime_fac_list[0] = 1
    i2, i3, i5 = 0, 0, 0
    
    nex_mul_2 = prime_fac_list[i2] * 2
    nex_mul_3 = prime_fac_list[i3] * 3
    nex_mul_5 = prime_fac_list[i5] * 5
    
    for i in range(1, num):
        prime_fac_list[i] = min(nex_mul_2,
                                nex_mul_3,
                                nex_mul_5)
        if prime_fac_list[i] == nex_mul_2:
            i2 += 1
            nex_mul_2 = prime_fac_list[i2] * 2
        if prime_fac_list[i] == nex_mul_3:
            i3 += 1
            nex_mul_3 = prime_fac_list[i3] * 3
        if prime_fac_list[i] == nex_mul_5:
            i5 += 1
            nex_mul_5 = prime_fac_list[i5] * 5
        
    return prime_fac_list[-1]

        
if __name__ == '__main__':
    n = 150
    res = ugly_numbers(n)
    print("Output: {0}".format(res))
