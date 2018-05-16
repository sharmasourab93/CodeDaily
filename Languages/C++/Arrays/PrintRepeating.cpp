//Print repeating numbers
#include<iostream>
#include<stdlib.h>
using namespace std;
void printrepeating(int arr[],int size){
	int *count=(int*)calloc(sizeof(int),size-2);
	int i;
	 cout<<"Repeating elements are:"<<endl;
	 for(i=0;i<size;i++){
	 	if(count[arr[i]]==1)
	 		cout<<arr[i]<< " ";
	 	else{
	 		count[arr[i]]++;
		 }
	 }
}
int main(){
	int arr[]={4,2,4,5,2,3,1};
	int size=sizeof(arr)/sizeof(arr[0]);
	printrepeating(arr,size);
}
