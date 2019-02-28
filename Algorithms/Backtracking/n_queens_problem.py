"""
Python: Back Tracking Algorithms
        N Queen's Problem
Source: Geeksforgeeks
"""


N = 4


# Print the Chess board function
def print_board(board):

    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


# Validates if the matrix on the board
# is safe for a Queen's placement
def is_safe(board, row, col):

    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


# Utility N Queens function for recursive call operation
def solve_nqutil(board, col):

    if col >= N:
        return True

    for i in range(N):

        if is_safe(board, i, col):
            board[i][col] = 1

            if solve_nqutil(board, col+1):
                return True

            board[i][col] = 0

    return False


# Primary N Queens driver function
def solve_nqueens():
    board = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]
             ]

    if not solve_nqutil(board, 0):
        print("Solution doesn't exist")
        return False

    print_board(board)


if __name__ == '__main__':
    solve_nqueens()