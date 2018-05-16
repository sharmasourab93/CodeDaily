//Row with maximum 1s in Naives method
#include<iostream>
#define M 4
#define N 4
using namespace std;
void findmax(int *array){
	int max=array[0];
	int index=0;
	for(int i=0;i<M;i++){
		if(array[i]>max){
			max=array[i];
			index=i;
		}
	}
	cout<<"Array with max number of 1s is "<<index;
}
void maxrow(int a[M][N]){
	int m=M;
	int n=N;
	int max_count[M]={0};
	for(int i=0;i<M;i++){
		for(int j=0;j<N;j++){
			if(a[i][j]==1){
				max_count[i]+=1;
			}
		}
	}
	findmax(max_count);
	
}
int main(){
	int array[M][N]={{1,1,1,1},{0,0,1,1},{0,1,1,1},{0,0,0,0}};
	maxrow(array);
}
