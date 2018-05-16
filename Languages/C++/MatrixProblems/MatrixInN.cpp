//Matrix Operations
#include<iostream>
#define N 4
using namespace std;
int main(){
	int mat[N][N]={{10,20,30,40},
				   {15,25,35,45},
				   {27,29,37,48},
				   {32,33,39,50}};
	int i=0,j=N-1;
	int x=29;
	while(i<N&& j>=0){
		if(mat[i][j]==x){
			cout<<"i: "<<i<<" "<<"j: "<<j<<endl;
		}
		if(mat[i][j]>x){
			j--;
		}else{
			i++;
		}
	}
	
}
