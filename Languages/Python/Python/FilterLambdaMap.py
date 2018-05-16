#using map
def cube(x):
    return x**2
print("Map Examples")
#Just prints the byte code
for i in map(cube,range(10)):print(i)

#First parentheses contains a lambda form that is
# a squaring function and second parentheses represents
#calling lambda
print((lambda x:x**2)(5))
print((lambda x,y:x*y)(3,4))
x=(lambda x:x**2)(5)
print("See this",x)

#Filter Examples
def cube(x):
    return x**3
cubes=map(cube,range(10))
for x in cubes:
    print(x)
x=filter(lambda x:x>9 and x<60,cubes)
for y in x:
    print(y)
