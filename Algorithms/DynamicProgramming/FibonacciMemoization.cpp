//Dynamic Programming\
//Memoization
#include<iostream>
#define MAX 100
#define NIL -1
#include<time.h>
using namespace std;
int lookup[MAX];
void _initialize(){
	int i;
	for(i=0;i<MAX;i++){
		lookup[i]=NIL;
	}
}
int fib(int n){
	if(lookup[n]==NIL){
		if(n<=1){
			lookup[n]=n;
		}else{
			lookup[n]=fib(n-1)+fib(n-2);
		}
	}
	return lookup[n];
}
int main(){
	int n=40;
	_initialize();
	double begin=clock();
	cout<<"Fibonnacci number is"<<fib(n);
	double end=clock();
	int time=(double)(end-begin);
	cout<<"\n TIme takne "<<time;
	
}

