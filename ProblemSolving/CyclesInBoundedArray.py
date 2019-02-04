#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the number_of_cycles function below.
def number_of_cycles_util(arr, x, y, string):
    arr[x], arr[y]=arr[y], arr[x]
    if arr[x]==y:
        "arr["+arr[y]+"]", end="->") else:
        number_of_cycles_util(arr, arr[x], y)


def number_of_cycles(arr):
    for i in range(len(arr)):
        if i!=arr[i]:
            number_of_cycles(arr, i, arr[i])
            print("arr["+str(arr[i])+"]")


if __name__=='__main__':