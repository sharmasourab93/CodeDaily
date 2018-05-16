//Search an element in a sorted and rotated array
#include<iostream>
using namespace std;
int pivotIndex(int arr[],int l,int r, int key){
	/*if(l<r){
		int mid=(l+r)/2;
		if(arr[mid]==key){
			return mid;
		}else if(arr[mid]<key){
			pivotIndex(arr,mid+1,r,key);
		}else if (arr[mid]>key){
			pivotIndex(arr,l,mid-1,key);
		}
	}*/
	
}

int main(){
	int arr[]={5,6,7,8,9,10,1,2,3};
	int key=3;
	int pivot=pivotIndex(arr,0,9,key);
	if(pivot==-1){
		cout<<"\nNot found!"<<endl;
	}else {
		cout<<"\nFound at index"<<pivot<<endl;
	}
}
