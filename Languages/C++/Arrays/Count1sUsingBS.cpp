//Using BS for counting 1s in a boolean array
#include<iostream>
using namespace std;
int countOnes(bool *arr,int low, int high){
	if(high>=low){
		//get the middle index
		int mid=low+(high-low)/2;
		//check if the element at middle index is last 1
		if((mid==high||arr[mid+1]==0)&&(arr[mid]==1)){
			return mid+1;
		}
		//If element is not last 1, recur for right side
		if(arr[mid]==1){
			return countOnes(arr,(mid+1),high);
		}
		//else recur for left side
		return countOnes(arr,low,mid-1);
	}
}
int main(){
	bool arr[]={1,1,1,1,1,0,0,0};
	int n=sizeof(arr)/sizeof(arr[0]);
	cout<<"\nCount of 1s in given array is "<<countOnes(arr,0,n-1);
}
