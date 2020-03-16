"""
Python: Dynamic Programming
        Longest Increasing Sub-sequence
        i.  Optimal Sub-structure Solution
        ii. Overlapping Sub-problems Solution
        
The Longest Increasing Sub-sequence (LIS) problem is to find
the length of the longest sub-sequence of a given sequence such that
all elements of the sub-sequence are sorted in increasing order.
"""
global maximum


# Optimal Sub-structure utility solution
def lis_optimal_util(array, num):

				global maximum

				if num == 1:
								return 1
				
				# max_ending here is the length of LIS
				# ending with array[num-1]
				max_ending = 1
				
				# Recursively get all LIS ending with arr[0], arr[1] .. arr[num-2]
				# If arr[num-1] is smaller than arr[n-1], and max ending with
				# arr[num-1] needs to be updated, then update it.
				for i in range(1, num):
								res = lis_optimal_util(array, i)
								if array[i-1] < array[num-1] and res + 1 > max_ending:
												max_ending = res + 1
				
				# Compare max_ending with overall maximum.
				# and update the overall maximum if needed
				maximum = max(maximum, max_ending)
				
				return max_ending


# Optimal Sub-structure solution
def list_optimal(array):
				"""
				To make use of recursive calls,
				This function must return two things:
				
				1. Length of LIS ending with element arr[len(arr)-1].
							We use max_ending for this purpose
				2. Overall maximum as the LIS may end with an element
							before arr[len(arr)-1] max_ref is used for this purpose.
				
				The value of LIS of full array of size n is stored in
				*max_ref which is our final result
				"""
				global maximum
				
				size = len(array)
				maximum = 1
				
				lis_optimal_util(array, size)
				
				return maximum


# Overlapping Sub-problem Solution
def lis_overlapping(array):
				
				size = len(array)
				
				lis = [1] * size
				
				for i in range(1, size):
								for j in range(0, i):
												if array[i] > array[j] and lis[i] < lis[j] + 1:
																lis[i] = lis[j] + 1
																
				maxi = 0
				
				for i in range(size):
								maxi = max(maxi, lis[i])
								
				return maxi
				
				
				
if __name__ == '__main__':
				
				# Call to Optimal LIS method
				arr = [10, 22, 9, 33, 21, 50, 41, 60]
				print("Finding length of LIS",
				      "\nUsing Optimal Sub-structure ")
				print(list_optimal(arr))
				
				# Call to LIS Overlapping method
				print("Finding length of LIS",
										"\nUsing Overlapping Sub-problems")
				print(lis_overlapping(arr))