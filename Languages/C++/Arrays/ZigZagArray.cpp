#include<iostream>
using namespace std;
void zigzag(int arr[],int n){
	bool flag=true;
	for(int i=0;i<=n-2;i++){
		if(flag){
			if(arr[i]>arr[i+1]){
				swap(arr[i],arr[i+1]);
			}else{
				if(arr[i]<arr[i+1]){
					swap(arr[i],arr[i+1]);
				}
			}
		}
		flag=!flag;
	}
}
int main(){
	int arr[]={4,3,7,8,6,2,1};
	int n=sizeof(arr)/sizeof(arr[0]);
	zigzag(arr,n);
	for(int i=0;i<n;i++){
		cout<<arr[i]<<" ";
	}
}
