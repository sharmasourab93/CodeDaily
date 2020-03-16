"""
Python: Dynamic Programming (DP)
        Overlapping Sub-problems
        i. Top Down Method (Memoization)
       ii. Bottom Down Method (Tabulation)

Dynamic Programming combines solutions to sub-problems.
DP is mainly used when solutions of the same sub-problems are needed
and computed solutions of sub-problems are stored in a table
for avoiding re-computation.

For example,
Binary Search doesn't have common sub-problems.
Whereas, recursive approach of Fibonacci Numbers have many
sub-problems which are solved again and again.
"""


# Top Down Method
def fib_top_down(look_up, num):
				"""
				The memoized program for a problem is similar
				to the recursive version with a small modification that
				it looks into a lookup table before computing solutions.
				We initialize a lookup array with all initial values as NIL.
				Whenever we need the solution to a sub-problem,
				we first look into the lookup table.
				If the precomputed value is there then we return that value,
				otherwise, we calculate the value and
				put the result in the lookup table so that it can be reused later
				"""
				
				if num == 0 or num == 1:
								look_up[num] = num
								
				if look_up[num] is None:
								look_up[num] = fib_top_down(look_up, num-1) + \
																							fib_top_down(look_up, num-2)
				
				return look_up[num]


# Bottom Up Approach
def fib_bottom_up(num):
				"""
				The tabulated program for a given problem builds a table in
				bottom up fashion and returns the last entry from table.
				For example,
				for the same Fibonacci number,
				we first calculate fib(0) then fib(1) then fib(2) then fib(3) so on.
				So literally, we are building the solutions of sub-problems bottom-up.
				"""
				
				f = [0] * (num + 1)
				f[1] = 1
				
				for i in range(2, num + 1):
								f[i] = f[i-1] + f[i-2]
				
				return f[num]


if __name__ == '__main__':
				
				# For calling top down method
				n = 34
				lookup = [None] * 101
				print("Fibonacci number using Top down approach:")
				print(fib_top_down(lookup, n))
				
				# For calling bottom up method
				n = 9
				print("Fibonacci number for Bottom Up approach is:")
				print(fib_bottom_up(n))