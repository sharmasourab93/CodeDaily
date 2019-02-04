import math
import os
import re
import sys
def CountNaturalNumber(n):
    rang=list(range(1,n+1))
    new_range=[]
    for i in rang:
        if len(str(i))==1:
            new_range.append(i)
        else:
            l1=list(str(i))
            if int(l1[0])<=int(l1[len(l1)-1]):
                new_range.append(int(''.join(l1)))
            else:
                pass
            #permuteString(list(str(i)),0,len(list(str(i)))-1,new_range)
    print(new_range,len(new_range))
CountNaturalNumber(21)



