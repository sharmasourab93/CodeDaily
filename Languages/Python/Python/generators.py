"""
Python : Generator Functions
"""


# Example 1: To Generate the next square
def next_square():
				i = 1
				while i < 10 and True:
								yield i * i						# Returns the value of i*i
								i = i + 2								# Returns i+2 value in next iteration


# Example 2: Sample Generator Method
def sample_generator():
				i = 1
				while i < 7 and True:
								yield i * i							# Retains value of i
								i += 1											 # Unlike a method


print("In next_square")
for num in next_square():
				if num > 15:
								break
				
				print(num)

print("In sample_generator")
for i in sample_generator():
				print(i)