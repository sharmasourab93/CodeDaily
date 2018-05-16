#include<iostream>
using namespace std;
int SIZE;
int getmatrix(int c[5][5]){
	int i,a,b;
	cout<<"\nGet the matrix dimension";
	cin>>i;
	SIZE=i;
	for(a=0;a<i;a++){
		for(b=0;b<i;b++){
			cout<<"\nInput for a["<<a<<"]["<<b<<"]:";
			cin>>c[a][b];
		}
	}
	return(c[i][i]);
}
int check(int a[5][5]){
	int j=1,x,k;
	for(int i=0;i<SIZE;i++){
		for(j=0;j<SIZE;j++){
				if(a[i][j]>a[i][j+1]){
					cout<<"\nInValid Row "<<i;
					break;
				}
				else{
					if(j==SIZE-1){
						cout<<"\nValid row "<<i;
						break;
					}else{
						continue;
					}
				}
				return 0;
			}}}
			
int main(){
	cout<<"\n The matrix Program";
	int a[5][5];
	getmatrix(a);
	check(a);
	
}

