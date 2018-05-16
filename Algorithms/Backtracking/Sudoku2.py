def print_Solution(arr):
    for i in range(9):
        for j in range(9):
            print(arr[i][j],end=" ")
        print()

def find_empty_location(arr,l):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j]==0:
                l[0]=i
                l[1]=j
                return True
    return False

def used_in_row(arr,row,num):
    for i in range(9):
        if arr[row][i]==num:
            return True
    return False

def used_in_col(arr,col,num):
    for i in range(9):
        if arr[i][col]==num:
            return True
    return False

def used_in_box(arr,row,col,num):
    for i in range(3):
        for j in range(3):
            if arr[i+row][j+col]==num:
                return True
    return False

def check_if_location_is_safe(arr,row,col,num):
    return not used_in_box(arr,row-row%3,col-col%3,num) and not used_in_row(arr,row,num) and not used_in_col(arr,col,num)

def solve_sudoku(arr):

    l=[0,0]
    if not find_empty_location(arr,l): return True
    row=l[0]
    col=l[1]

    for num in range(1,10):
        if check_if_location_is_safe(arr,row,col,num):
            arr[row][col]=num
            if solve_sudoku(arr): return True
            arr[row][col]=0
    return False

