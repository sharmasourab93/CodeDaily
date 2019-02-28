"""
Python: Using Filter
"""


def cube(x):
    return x**3

cubes = map(cube, range(10))

store_filters = filter(lambda x: x > 9 and x < 100, cubes)

for i in store_filters:
    print(i)