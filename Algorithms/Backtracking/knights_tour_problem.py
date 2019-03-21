"""
Python: Backtracking Algorithm
        Knights Tour Problem
"""


N = 8


# To print the solution matrix
def print_solution(solution_matrix):
    for i in range(N):
        for j in range(N):
            print(solution_matrix[i][j], end=" ")
        print()


# To check if the given matrix row and column
# falls within the matrix boundary
def is_bool_safe(x, y, solution_matrix):

    return 0 <= x < N and \
           0 <= y < N and \
           solution_matrix[x][y] == -1


# Knight's Tour Utility Function
def solve_knights_tour_util(x, y, move_i,
                            solution_matrix,
                            x_move, y_move):

    if move_i == N*N:
        return True

    for k in range(N):
        next_x = x + x_move[k]
        next_y = y + y_move[k]

        if is_bool_safe(next_x, next_y, solution_matrix):
            solution_matrix[next_x][next_y] = move_i

            if solve_knights_tour_util(next_x, next_y, move_i+1,
                                       solution_matrix,
                                       x_move, y_move):
                return True

            else:
                solution_matrix[next_x][next_y] = -1  #BackTrack

    return False


# Primary Driver Function
# for solving Knight's Tour problem
def solve_knights_tour():
    solution_matrix = [[-1 for j in range(N)] for i in range(N)]
    solution_matrix[0][0] = 0

    x_move = [2, 1, -1, -2, -2, -1, 1, 2]
    y_move = [1, 2, 2, 1, -1, -2, -2, -1]

    if not solve_knights_tour_util(0, 0, 1,
                                   solution_matrix,
                                   x_move, y_move):

        print("Solution doesn't exist")
        return False

    else:
        print_solution(solution_matrix)
        return True


if __name__ == '__main__':
    solve_knights_tour()
