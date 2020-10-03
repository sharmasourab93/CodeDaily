"""
Problem Solving: Code Chef
Today is Chef's birthday and he is looking forward to his gift.
As usual, the gift is hidden and Chef has to follow
    a sequence of N instructions to reach it.

Initially, Chef is standing in the cell (0,0) of a two-dimensional grid.
 The sequence of instructions is given as a string S.
 If we denote Chef's current cell by (x,y), each character of S
    corresponds to an instruction as follows:

'L' means to go left, i.e. to the cell (x−1,y)
'R' means to go right, i.e. to the cell (x+1,y)
'U' means to go up, i.e. to the cell (x,y+1)
'D' means to go down, i.e. to the cell (x,y−1)
In addition,
Chef should never perform multiple consecutive moves along the same axis of the grid.
If there are multiple consecutive instructions to move along
    the same axis (left/right or up/down),
    he should perform only the first of these moves.

Find the cell (xg,yg) which contains the hidden gift.
"""
    

def gift_src(pattern):
    x, y, lp = 0, 0, None
    for i in pattern:
        if i == 'L' and (lp != 'R' and lp != 'L'):
            x = x - 1
            lp = i
        elif i == 'R' and (lp != 'L' and lp != 'R'):
            x = x + 1
            lp = i
        elif i == 'U' and (lp != 'U' and lp != 'D'):
            y = y + 1
            lp = i
        elif i == 'D' and (lp != 'U' and lp != 'D'):
            y = y - 1
            lp = i
        else:
            continue
    
    return x, y


if __name__ == '__main__':
    num_tests = int(input())
    for i in range(num_tests):
        n = int(input())
        string = input()
        res = (gift_src(string))
        (x, y) = res
        print("{0} {1}".format(x, y))
    
    # gift_src('LRULLUDU')
    # gift_src('LLLRUUD')
    # gift_src('LLLUR')
