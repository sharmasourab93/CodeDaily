"""
Activity Selection problem
s[] = An array that contains start time of all activities
f[] = An array that contains finish time of all activities
"""


def print_max_activities(s, f):
				n = len(f)    #n = total number of activities
				print("The following activities are selected")
				
				i = 0
				print(i)
				
				for j in range(n):
								if s[j] >= f[i]:
												print("{0} >= {1}".format(s[j], f[i]), end=" -->")
												#print(i, j)
												i = j


s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
print_max_activities(s, f)