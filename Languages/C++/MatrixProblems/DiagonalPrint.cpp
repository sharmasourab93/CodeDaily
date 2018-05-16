//Diagnol print 
#include<iostream>
#define ROW 4
#define COL 5
using namespace std;
//A utility function to fund min of two integers
int min(int a,int b){
	return ((a<b)?a:b);
}
//A utility function to find min of three integers
int min(int a,int b,int c){
	return min(min(a,b),c);
}
//A utility function to find max of two integers
int max(int a,int b){
	return((a>b)?a:b);
}
void diagonalOrder(int matrix[][COL]){
	for(int line=1;line<+(ROW+COL-1);line++){
		int start_col=max(0,line-ROW);
		int count=min(line,(COL-start_col),ROW);
		for(int j=0;j<count;j++){
			cout<<matrix[min(ROW,line)-j-1][start_col+j]<<" ";
		}
		cout<<endl;
	}
}
void printMatrix(int matrix[ROW][COL]){
	for(int i=0;i<ROW;i++){
		for(int j=0;j<COL;j++){
			cout<<matrix[i][j];
		}
		cout<<endl;
	}
}
int main(){
	int M[ROW][COL]={{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16},{17,18,19,20}};
	cout<<"Given Matrix:"<<endl;
	printMatrix(M);
	cout<<"Diagnal printing of Matrix is "<<endl;
	diagonalOrder(M);
}
