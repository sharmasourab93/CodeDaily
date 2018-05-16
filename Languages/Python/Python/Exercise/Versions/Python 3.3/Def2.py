#!/usr/bin/env python 3.1
def add(a,b):
    "Hello Friends this functions is about to add two numbers"
    if a>b:
        raise TypeError("Such Kind of a File is Misappropriate")
    else:
        c=a+b
        print(c)
    



def main():
    add(2,3)
    add(232343433,43435454544)
    x=int(input("Enter a Numero"))
    y=int(input("Enter a Numero"))
    add(x,y)

main()
