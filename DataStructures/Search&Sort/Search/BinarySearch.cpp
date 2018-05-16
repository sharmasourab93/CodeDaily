//Binary search
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
int main(){
	int arr[]={2,40,1,10,23};
	int size=((sizeof(arr))/(sizeof(arr[0])));
	int bs=binarySearch(arr,0,size-1,22);
	if(bs==-1){
		cout<<"Element doesn't exist";
	}else{
		cout<<"Element exists at "<<bs+1;	
	} 
}
