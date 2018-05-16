N=8
def isboolSafe(x,y,solMat):
    return (x>=0 and x<N and y>=0 and y<N and solMat[x][y]==-1)

def solveKTUtil(x,y,movei,solMat,xMove,yMove):
    print("In SolveKTUtil")
    if movei==N*N:
        return True
    k=0
    next_y=0
    next_x=0
    for k in range(N):
        next_x=x+xMove[k]
        next_y=y+yMove[k]
        if isboolSafe(next_x,next_y,solMat)==True:
            solMat[next_x][next_y]=movei
            if solveKTUtil(next_x,next_y,movei+1,solMat,xMove,yMove)==True:
                return True
            else:
                solMat[next_x][next_y]=-1#BackTrack
    return False

def solveKT():
    print("In SolveKT")
    solMat=[[-1 for j in range(N)] for i in range(N)]
    xMove=[2,1,-1,-2,-2,-1,1,2]
    yMove=[1,2,2,1,-1,-2,-2,-1]
    solMat[0][0]=0
    if solveKTUtil(0,0,1,solMat,xMove,yMove)==False:
        #print("After SolveKTUtil")
        print("Solution doesn't exist")
        return False
    else:
        printSolution(solMat)
    return True

def printSolution(solMat):
    for i in range(N):
        for j in range(N):
            print(solMat[i][j],end=" ")
        print()

if __name__ == '__main__':
    solveKT()
