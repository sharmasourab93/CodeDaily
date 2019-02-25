#Filter Examples
def cube(x):
    return x**3


cubes = map(cube, range(10))
print("Iterating Cubes")
for c in cubes:
    print(c)


store_filter = filter(lambda x: x > 9 and x < 60, cubes)
print("Iterating Filter variable")
for sf in store_filter:
				print(sf)