"""
Greedy Algorithm to find the minimum number of coins:-
	1. Initialize result as empty set
	2. Find the largest denomination that is smaller than V.
	3. Add found denomination to result.
	 		Subtract value of found denomination from V
	4. If V becomes 0, then print result
										Else repeat Step 2 & Step 3
"""
from collections import Counter


def findcoins(sum, denominations):
				d_size = len(denominations)
				result = []
				
				for i in range(d_size-1, -1, -1):
								
								while sum >= denominations[i]:
												sum = sum - denominations[i]
												result.append(denominations[i])
				
				return dict(Counter(result))


denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
get_dict = findcoins(93, denominations)
print("We need: - ")

for k, v in get_dict.items():
				print(str(v), "Nos of ", str(k), "Rs Coin")