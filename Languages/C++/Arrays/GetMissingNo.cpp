//Get Missing numbers
#include<iostream>
using namespace std;
int findMax(int *arr, int size){
	int max=arr[0];
	for(int i=1;i<size;i++){
		if(arr[i]>max) max=arr[i];
	}
	return max;
}
void getMissingNo(int *arr,int size){
	int max=findMax(arr,size);
	int total=(max*(max+1))/2;
	for(int i=0;i<size;i++)
		total-=arr[i];
	cout<<"The missing element is "<<total<<endl;
}
int main(){
	int arr[]={1,2,3,4,5,6,8};
	int size=sizeof(arr)/sizeof(arr[0]);
	getMissingNo(arr,size);
}
