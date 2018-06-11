import os
import base64
def secure_rand(len=8):
    token=os.urandom(len)
    return base64.b64encode(token)

print(secure_rand())


import random
from math import floor as f
def get_promo_code(num_chars):
    code_chars='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code=''
    for i in range(0,num_chars):
        #slice_start=random.randint(0,len(code_chars)-1)
        #code+=code_chars[slice_start:slice_start+1]
        code+=code_chars[f(random.randint(0,len(code_chars)-1))]

    return code

print(get_promo_code(8))
