// 0 and X 
#include<iostream>
#define M 3
#define N 3
using namespace std;
void printArray(char a[M][N],int m,int n){
	for(int i=0;i<m;i++){
		for(int j=0;j<n;j++){
			cout<<a[i][j]<<" ";
		}
		cout<<endl;
	}
}
void tictac(char a[N][M],int m, int n){
	char x='X';
	int a1=m,a2=n;
	
	int i,k=0,l=0;
	while(k<m&&l<n){
		for(i=l;i<m;i++){
			a[k][i]='X';
			//cout<<a[k][i]<<" ";
		}
		k++;
		for(i=k;i<n;i++){
			a[i][n-1]='X';
			//cout<<a[i][n-1]<<" ";
		}
		n--;
		if(k<m){
			for(i=m-1;i>=1;i--){
				a[m-1][i]='X';
			//	cout<<a[m-1][i]<<" ";
			}
			m--;
		}
		if(l<n){
			for(i=1;i<=n;i++){
				a[l][i]='X';
			//	cout<<a[l][i]<<" ";
			}
			l++;
			}
			//cout<<endl;
			x=(x=='O')?'X':'O';
		}
	printArray(a,a1,a2);
}
int main(){
	int m=3,n=3;
	int array[m][n];
	
}
