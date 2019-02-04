""" Optimal Substructure Example """
global maximum


def _lis(arr, n):
				global maximum
				if n == 1:
								return 1
				
				max_ending_here = 1
				
				for i in range(1, n):
								res = _lis(arr, i)
								if arr[i-1] < arr[n-1] and res+1 > max_ending_here:
												max_ending_here = res+1
												#print(max_ending_here, end=",")
				maximum = max(maximum, max_ending_here)
				
				return max_ending_here


def lis(arr):
				global maximum
				n = len(arr)
				maximum = 1
				_lis(arr, n)
				return maximum


print("Optimal Substructure")
arr1 = [10, 22, 33, 21, 50, 41, 60]
n = len(arr1)
print("Length of lis is {0}".format(lis(arr1)))


""" Overlapping Subproblem """


#Tabulated Method
def lis1(arr):
				n = len(arr)
				lis = [1] * n
				for i in range(1, n):
								for j in range(0, i):
												if arr[i] > arr[j] and lis[i] < lis[j] + 1:
																lis[i] = lis[j] + 1
				
				maximum = 0
				
				for i in range(n):
								maximum = max(maximum, lis[i])
								
				return maximum


print("Overlapping Subproblem")
arr = [10, 22, 9, 33, 21, 50, 41, 60]
print("Length of lis is ", lis1(arr))