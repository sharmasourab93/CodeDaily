/*Insertion Sort*/
#include<iostream>
using namespace std;
//Function to swap 2 numbers
void swap(int * a, int* b){
	int temp;
	temp=*a;
	*a=*b;
	*b=temp;
}
//Insertion Sort Function
void insertionSort(int a[],int n){
	int i,j,min;
	for(i=1;i<n;i++){
		min=a[i];
		j=i-1;
		while(j>=0&&a[j]>min){
			a[j+1]=a[j];
			j--;
		}
		a[j+1]=min;
	}
}
//Prints an array
void printarr(int a[],int n){
	for(int l=0;l<n;l++){
		cout<<"\t"<<a[l];
	}
}
int main(){
	int a[]={10,9,8,1,6,5,4};
	int size=((sizeof(a))/sizeof(a[0]));
	insertionSort(a,size);
	printarr(a,size);
}

