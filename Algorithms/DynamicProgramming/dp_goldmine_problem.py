""""
Python: Dynamic Programming (DP)
        Goldmine Problem
"""


def goldmine_dp(gold_mat, M, N):
    
    gold_table = [[0 for i in range(N)] for j in range(M)]
    
    for col in range(N-1, -1, -1):
        for row in range(M):
            
            if col == N-1:
                right = 0
            else:
                right = gold_table[row][col+1]
                
            if row == 0 or col == N-1:
                right_up = 0
            else:
                right_up = gold_table[row-1][col+1]
            
            if row == M-1 or col == N-1:
                right_down = 0
            else:
                right_down = gold_table[row+1][col+1]
            
            gold_table[row][col] = gold_mat[row][col] + \
                max(right, right_up, right_down)
            
    res = gold_table[0][0]
    # print(gold_table)
    for i in range(1, M):
        res = max(res, gold_table[i][0])
    
    return res


if __name__ == '__main__':
    gold_mat = [[10, 33, 13, 15],
                [22, 21, 4, 1],
                [5, 0, 2, 3],
                [0, 6, 14, 2]]
    result = goldmine_dp(gold_mat, 4, 4)
    print("Result {0}".format(result))