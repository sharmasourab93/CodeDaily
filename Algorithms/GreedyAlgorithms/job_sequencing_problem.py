"""
Greedy Algorithm : Job Sequencing Problem
	1. Sort all jobs in decreasing order of profit
	2. Initialize the result sequence as first job 	in sorted order
	3. Do following for remaining n-1 Jobs:
				i. If Current job can fit in the current result \
				   without missing the deadline, Add current job to the result.
				ii. Else ignore the current job.
"""