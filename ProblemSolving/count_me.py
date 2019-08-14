"""
Count Me

Given an Array  of  integers and  queries. Each query is defined by three integers  ,  and .
You need to print the count of numbers which can divide  and lie in index range  to .

Input

First Line: , defining size of array
Second Line:  space separated integers, defining array .

Third Line: , total no of Queries.

Fourth Line:  space separated integers which define .

Fifth Line:  space separated integers which define .

Sixth Line:  space separated integers which define .

Output
Print answers of all queries as space separated integers.
"""


def cnt(a, x, r, z):
				count_array = []
				
				
				for j, k in zip(z, r):
								for i in range(j, k):
								
								
								#count_array.append(count)
				#return count_array
				

if __name__ == "__main__":
				N = 5
				A = [2, 1, 5, 18, 6]
				Q = 5
				L = [1, 3, 2, 5, 1]
				R = [5, 5, 4, 5, 4]
				X = [20, 36, 10, 13, 5]
				out = cnt(A, X, R, L)
				print(out)
