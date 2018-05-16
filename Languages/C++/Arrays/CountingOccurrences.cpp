//Number of occurences in a sorted array 
#include<iostream>
using namespace std;
int binarySearch(int arr[], int l, int r, int x){
	while(l<=r){
		int m=l+(r-l)/2;
		if(arr[m]==x){
			return m;
		}
		if(arr[m]<x){
			l=m+1;
		}
		if(arr[m]>x){
			r=m-1;
		}
	}
	return -1;
}
void countNumbers(int *array, int size){
	int count=0;
	for(int i=0;i<size;i++){
		if(array[i]==key){
			count++;
		}
	}
	cout<<"Total Count of key: "<<count<<endl;
}
int main(){
	int array[]={1,1,2,2,2,2,3,3,4,4,5,5,6};
	int size=sizeof(array)/sizeof(array[0]);
	int key;
	countNumbers(array,size);
}
