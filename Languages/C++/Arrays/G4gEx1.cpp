//Array Problems 
/*Given an array A[] and a number x, check for pair in A[] with sum as x*/
/*Write a C program that, given an array A[] of n numbers and another number x,
 determines whether or not there exist two elements in S whose sum is exactly x.*/
#include<iostream>
#define N 9
using namespace std;
int swap(int *a, int *b){
	int temp;
	temp=*a;
	*a=*b;
	*b=temp;
	return *a, *b;
}
void sortNsum(int array[N], int X){
	for(int i=0;i<N;i++){
		for(int j=0;j<N;j++){
			if(array[i]<array[j]){
				swap(&array[i], &array[j]);
			}
		}
	}
	for(int i=0;i<N;i++){
		cout<<array[i]<<endl;
	}
	cout<<"\n Sorted!"<<endl;
	for(int i=0;i<N;i++){
		for(int j=i+1;j<N;j++){
			if(array[i]+array[j]==X){
				cout<<array[i]<<" "<<array[j];
			}
		}
	}
}
int main(){
	int array[]={9,4,2,32,65,11,10,20,40};
	int x=21;
	int n=((sizeof(array))/(sizeof(array[0])));
	cout<<__TIME__<<endl;
	sortNsum(array,x);
	cout<<__TIME__<<endl;
}
