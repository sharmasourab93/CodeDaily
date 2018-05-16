//number rhombus
#include<iostream>
using namespace std;
void upperorder(int a,int x){
	int i=0,j;
		//loop within loop1
		for(j=x;j>0;j--){
		
		while(j>0 && a-j!=x){
			j--;
			cout<<a-j;
			
		}
	}
		cout<<a;	
		while(i<x && a-i!=x){
			i++;
			cout<<a-i;
		}
}
void rhombus(int a){
	int i,j,k;
	//loop 1;
	for(i=0;i<a;i++){
		upperorder(a,i);
		cout<<endl;
	}
}
int main(){
	int a,b,c;
	cout<<"\nEnter a number:";
	cin>>a;
	rhombus(a);
}
