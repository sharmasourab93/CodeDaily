#Testing the calling of a function from another function in python
def hello():
    "Hey this function will print execute the function"
    x=int(input("ENter the interger"))
    y=int(input("Enter another integer"))
    add(x,y)
def add(a,b):
    z= a+b
    print(z)
    return z
hello()
