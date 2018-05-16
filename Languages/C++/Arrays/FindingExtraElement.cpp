//Finding extra Element
#include<iostream>
using namespace std;
//Basic O(n) method
int findextra(int arr1[],int arr2[],int n){
	for(int i=0;i<n;i++){
		if(arr1[i]!=arr2[i]){
			return i;
		}
	}
	return n;
}
//BS O(log n) method
int BSfindextra(int arr1[],int arr2[], int n){
	int index=n;
	int left=0,right=n-1;
	while(left<=right){
		int mid=(left+right)/2;
		if(arr2[mid]==arr1[mid]){
			left=mid+1;
		}else{
			index=mid;
			right=mid-1;
		}
	}
	return index;
}
int main(){
	int arr1[]={2,4,6,8,10,12,13};
	int arr2[]={2,4,6,8,10,12};
	int n=sizeof(arr2)/sizeof(arr2[0]);
	
}
