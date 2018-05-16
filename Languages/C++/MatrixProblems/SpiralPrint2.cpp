//Spiral Print 
#include<iostream>
using namespace std;
#define N 4

int SpiralPrint(int m[N][N]){
	int i,k=0,l=0;
	int n=N-1;
	int n1=N-1;
	while(k<N &&l<N){
		for(i=l;i<n;++i){
			cout<<m[k][i]<<" ";
		}
		k++;
		for(int i=k;i<n;++i){
			cout<<m[i][n]<<" ";
		}
		n--;
		if(k<n1){
			for(i=n;i>=0;--i){
				cout<<" "<<m[n1-1][i];
			}
			n1--;
		}
		if(l<n){
			for(i=l;i<n;++i){
				cout<<" "<<m[i][l];
			}
			l++;
		}
		
		
	}
}
int main(){
	int mat[N][N]={{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}};
	SpiralPrint(mat);
	
}
