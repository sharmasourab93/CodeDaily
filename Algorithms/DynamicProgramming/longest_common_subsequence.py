"""
Python: Dynamic Programming (DP)
        Lowest Common Sub-sequence (LCS)

Given two sequences, find the length of the longest sub-sequence
present in both of them.

A sub-sequence is a sequence that appears in the same relative order
but not necessarily contiguous. For example: "abc", "abg", "bdf", "aeg",
"acefg", ... etc are sub-sequences of "abcdefg"
"""


# Optimal Sub-Structure Solution
def lcs_optimal(x, y):
				# TODO: LCS Optimal solution
    pass


"""
			For finding the complexity of the brute force approach,
			first to be known are the number of possible different
			sub-sequences of a string with length n, i.e.

			The number of combinations with 1 element are nC1.
			Number of combinations with 2 elements are nC2.
			Hence,
			nC0 + nC1 + nC2 + ... + nCn = 2 ^ n

			So string of length n has (2 ^ n) - 1 different possible
			sub-sequence.

			Hence the time complexity of brute force method is O(n * (2 ^ n)).
			Note: O(n) time to check if a sub-sequence is
			common to both the strings.
			
			Time complexity of the above naive recursive approach is
			O(2^n) in worst case and worst case happens
			when all characters of X and Y mismatch i.e., length of LCS is 0.j
"""


# Overlapping Sub-Problem Solution
# Naive Solution implementation
def lcs_overlapping(x, y):
				
				size_x, size_y = len(x), len(y)
				
				if size_x == 0 or size_y == 0:
								return 0
				
				elif x[size_x-1] == y[size_y-1]:
								return 1 + lcs_overlapping(x[:-1], y[:-1])
				
				else:
								return max(lcs_overlapping(x[:], y[:-1]),
																			lcs_overlapping(x[:-1], y[:]))


# Optimized Bottom Up Overlapping sub-problem solution
# Time complexity is far better compared to Naive solution
# Time Complexity is O(m * n)
def lcs_overlapping_optimized(x, y):
				
				size_x, size_y = len(x), len(y)
				
				seq = [[0] * (size_y + 1) for i in range(size_x+1)]
				
				# Building LCS[size_x+1][size_y+1]
				for i in range(size_x+1):
								for j in range(size_y+1):
												
												if i == 0 or j == 0:
																seq[i][j] = 0
												
												elif x[i-1] == y[j-1]:
																seq[i][j] = seq[i-1][j-1] + 1
																
												else:
																seq[i][j] = max(seq[i-1][j], seq[i][j-1])
				
				return seq[size_x][size_y]
				


if __name__ == '__main__':
				
				arr_x, arr_y = "AGGTAB", "GXTXAYB"
				print("Using LCS Overlapping method")
				print("Length of LCS is ", lcs_overlapping(arr_x, arr_y))
				
				# Calling Optimized overlapping method
				print("Using Optimized Overlapping LCS method")
				print("Lenght of LCS is", lcs_overlapping_optimized(arr_x, arr_y))