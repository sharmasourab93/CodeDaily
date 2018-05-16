//Maximum 1s using Binary Search 
#include<iostream>
#define C 4
#define D 4
using namespace std;
int arrayBS(int arr[], int low, int high){
	int mid=(low+high)/2;
	if(low<high){
		if(arr[mid]==1&&arr[mid-1]==0){
			return mid;
		}else if(arr[mid]==0){
			return arrayBS(arr,(mid+1),high);
		}else{
			arrayBS(arr,low,mid-1);
		}
	}
	return -1;
}
int rwoWithMax1s(int a[C][D]){
	int max_row=0,max=-1;
	int i,index;
	for(i=0;i<D;i++){
		index=arrayBS(a[i],0,C-1);
		if(index!=-1 && C-index>max){
			max=C-index;
			max_row=i;
		}
	}
	return max_row;
}
int main(){
	int array[C][D]={{1,1,1,1},{0,0,1,1},{0,1,1,1},{0,0,0,0}};
	cout<<rwoWithMax1s(array);
}
