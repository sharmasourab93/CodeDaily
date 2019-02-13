"""
Python: Two different methods to Generate Coupon Codes
"""
import os
import random
from math import floor
import base64


def secure_rand(len=8):
    token = os.urandom(len)
    return base64.b64encode(token)


def get_promo_code(num_chars):
    code_chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for i in range(0, num_chars):
        slice_start=random.randint(0, len(code_chars)-1)
        #code+=code_chars[slice_start:slice_start+1]
        code += code_chars[floor(slice_start)]

    return code


print(secure_rand())
print(get_promo_code(8))
