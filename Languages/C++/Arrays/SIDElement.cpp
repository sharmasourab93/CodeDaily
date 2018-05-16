//Search insert delete an insorted array 
#include<iostream>
using namespace std;
#define N 7
//Operation to search an element in an array
int search(int arr[],int n,int key){
	int i;
	for(i=0;i<n;i++){
		if(arr[i]==key)
		return i;
	}
	return -1;
}
//operation to insert an element in an array
int insert(int arr[],int n,int key,){
	if(n>=N) return n;
	arr[n]=key;
	return (n+1);
}
//operation to delete an element from an array
int del(int arr[],int n,int key){
	int pos=search(arr,n,key);
	cout<<"\nSearching element: "
	if(pos==-1){
		cout<<"\n Not found"<<endl;
		return n;
	}
	cout<<"\nElement found."<<endl
	int i;
	for(i=pos;i<n-1;i++){
		arr[i]=arr[i+1];
	}
	cout<<
	return n-1;
}
int printarray(int arr[],int n){
	cout<<" Printing the array: "<<endl;
	for(int i=0;i<n;i++){
		cout<<arr[i]<<" ";
	}
}
//Driver function
int main(){
	int i;
	int arr[N]={10,20,40,30,50,23,98};
	int n=sizeof(arr)/sizeof(arr[0]);
	int key=30;
	cout<<"\nDeleting "<<key<<endl;
	int z=del(arr,n,key);
	printarray(arr,n);
	insert
	
}
