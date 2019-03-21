"""
Python: Backtracking Algorithm
        Sudoku
"""


# Printing grids on the Sudoku Board
def print_grid(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j], end=" ")
        print()


# Finding Empty location
def find_empty_location(arr, store):
    for row in range(9):
        for col in range(9):
            if arr[row][col] == 0:
                store[0], store[1] = row, col
                return True

    return False


# To Validate if a number has been used in the row
def used_in_row(arr, row, num):
    for i in range(9):
        if arr[row][i] == num:
            return True

    return False


# To Validate if a number has been used in the column
def used_in_col(arr, col, num):
    for i in range(9):

        if arr[i][col] == num:
            return True

    return False


# To Validate if a number has been used in the box/sub-matrix
def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if arr[i+row][j+col] == num:
                return True

    return False


# Utility function which validates row, column and box
def is_location_safe(arr, row, col, num):

    return not used_in_row(arr, row, num) and \
           not used_in_col(arr, col, num) and \
           not used_in_box(arr, row-row%3, col-col%3, num)


# Driver Function
def solve_sudoku(arr):
    store = [0, 0]

    if not find_empty_location(arr, store):
        return True

    row = store[0]
    col = store[1]

    for num in range(1, 10):
        if is_location_safe(arr, row, col, num):
            arr[row][col] = num

            if solve_sudoku(arr):
                return True

            arr[row][col] = 0

    return False


if __name__ == '__main__':
    # grid = [[0 for x in range(9)] for y in range(9)]
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]
            ]

    if solve_sudoku(grid):
        print_grid(grid)

    else:
        print("No Solution exists")