//Knight's Tour Problem
//From Geeks4Geeks
#include<iostream>
#define N 8
using namespace std;

int solveKTUtil(int x,int y, int movei, int sol[N][N],int xMove[],int yMove[]);
//A utility function to check if i,j are valid indexes for N*N chess board
bool isSafe(int x, int y,int sol[N][N]){
	return (x>=0 &&x<N &&y>=0 &&y<N &&sol[x][y]==-1);
}
//A function to print the solution of the Knight's tour
void printSolution(int sol[N][N]){
	for(int x=0;x<N;x++){
		for(int y=0;y<N;y++){
			if(sol[x][y]%10<1){
				cout<<sol[x][y]<<"  ";
			}else{
				cout<<sol[x][y]<<" ";
			}
		}
		cout<<endl;
	}
}
//Primary Driver function which solves the problem.
/*
   This function solves the Knight Tour problem using
   Backtracking.  This function mainly uses solveKTUtil()
   to solve the problem. It returns false if no complete
   tour is possible, otherwise return true and prints the
   tour.
   Please note that there may be more than one solutions,
   this function prints one of the feasible solutions.  
*/
bool solveKT(){
	int sol[N][N];
	//Initializing Solution matrix
	for(int x=0;x<N;x++){
		for(int y=0;y<N;y++)
			sol[x][y]=-1;
	}
	//xMove and yMove decide the solution, which means 
	//xMove for x coordinate
	//yMove for y coordinate
	int xMove[8]={2,1,-1,-2,-2,-1,1,2};
	int yMove[8]={1,2,2,1,-1,-2,-2,-1};
	//Since the knight is initially in the first block [0][0]
	sol[0][0]=0;
	if(solveKTUtil(0,0,1,sol,xMove,yMove)==false){
		cout<<"Solution does not exist.";
		return false;
	}else{
		printSolution(sol);
	}
	return true;
}
//Returns the result based on the values on the respective position
/* 
	A recursive utility function to solve Knight Tour
   problem 
*/
int solveKTUtil(int x,int y,int movei,int sol[N][N],int xMove[N],int yMove[N]){
	int k, next_x,next_y;
	//movi==N*N stands for the total number of time the solution has recured and returned true;
	//Hence meaning that This solution is corrent
	if(movei==N*N){
		return true;
	}
	//If Movei!=N*N
	//Look for possible solutions in the next moves. And if it solutions is withing
	/* Try all next moves from the current coordinate x, y */
	for(k=0;k<8;k++){
		next_x=x+xMove[k];
		next_y=y+yMove[k];
		if(isSafe(next_x,next_y,sol)){
			sol[next_x][next_y]=movei;//Increments with every recursion
			if(solveKTUtil(next_x,next_y,movei+1,sol,xMove,yMove)==true){
				return true;
			}else{
				sol[next_x][next_y]=-1;//backtracking
				//This signifies that the current position can be accessed from any other step
				//Hence it is marked again as -1.
			}
		}		
	}
	return false;
}
int main(){
	solveKT();
	return 0;
}
