//Rat in a Maze problem
//Self solved
#include<iostream>
#define N 4
using namespace std;
//Checks if the coordinates are safe or not
bool isSafe(int x, int y, int mat[N][N]){
	if(x>=0&&x<N&&y>=0&&y<N&&mat[x][y]==1) return true;
	return false;
}
//Prints the Maze Matrix
void printMaze(int newMat[N][N]){
	cout<<"\nThe Matrix is:"<<endl;
	for(int x=0;x<N;x++){
		for(int y=0;y<N;y++){
			cout<<newMat[x][y]<<" ";
		}
		cout<<endl;
	}
}
//A recursive Utility function which traverses through matrix
//And returns if the solution is true or not
int MazeUtil(int movei,int x, int y,int mat[N][N],int newMat[N][N]){
	/*if(movei==2*N-1){
		return true;
	}*/
	
	if(x==N-1&&y==N-1){
		newMat[x][y]=1;
		return true;
	}
	
	int k=1,l=1;
	while(k<N&&l<N){
		if(isSafe(x,y+l,mat)){
			movei+=1;
			newMat[x][y+l]=1;
			if(MazeUtil(movei,x,y+l,mat,newMat)==true)
				return true;
		}
		else if(isSafe(x+k,y,mat)){
			movei+=1;
			newMat[x+k][y]=1;
			if(MazeUtil(movei,x+k,y,mat,newMat)==true)
				return true;
		}else{
			newMat[x][y]==0;
			return false;
		}
	}
	//return false;
}
int Maze(int mat[N][N]){
	int newMat[N][N]={0};
	newMat[0][0]=1;
	if(mat[N-1][N-1]!=1){
		cout<<"Solution Doesn't exist."<<endl;
		return 0;
	}
	int i=0,j=0;
	if((MazeUtil(1,i,j,mat,newMat))==true){
		cout<<"Solution: ";
		printMaze(newMat);
	}else{
		cout<<"\nSolution Doesn't exist"<<endl;
	}
}
int main(){
	int matrix[N][N]={{1,0,0,0},{1,1,0,1},{0,1,0,0},{1,1,1,1}};
	printMaze(matrix);
	Maze(matrix);
}
