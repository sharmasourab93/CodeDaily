"""
Given a large series of number strings, return each
that might be potential lottery ticket pick. Note that a valid lottery
ticket satisfies the following properties
	
	1. The digit must form 7 unique numbers between 1 and 59
	
	2. Digits must be used in order. You cannot form a number using digit n and
	   digit n+10
				for Example: in 12345678, you can't use 1 and 3 to get 13 in your pick
 
 3. Every digit must be used exactly once. This means that you cannot use one
 			digit as a past of two different numbers.
 			Eg:in 1234567, you can't get 12 23 3 4 5 6 7
 			as the lottery pick as the digit 2 is being used in both 12 and 23
 
 4. All the digits must be used. Eg: If the sequence is 12345679, 1, 2, 3, 4, 5, 6, 7,
 			cannot be a lottery pick as the final digit 9 also must be used.
 			
Input Format:
The first line contains the number of number strings n
The next n lines contain a single number string each

Output Format
Print a single number string and a valid lottery pick separated "->"
e.g. 1234567 -> 1 2 3 4 5 6 7
If there is more than one valid lottery pick , print them in separate lines

Sample Input:
5
569815571556
4938532894754
1234567
472844278465445
0123456

Sample Output:

4938532894754 -> 49 38 53 28 9 47 54
1234567 -> 1 2 3 4 5 6 7
"""


def process_data(array):
				for i in array:
								if '0' == i[0]:
												continue
				    
				    
				    				
				    


if __name__ == "__main__":
				
				# Input N number of lines to process
				n = int(input())
				
				# Read n lines of input
				n_lines = []
				for i in range(n):
								n_lines.append(str(input()))
								
				process_data(n_lines)
				
				






















