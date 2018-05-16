//Merge two sorted Arrays
#include<iostream>
using namespace std;
void print(int *array, int size){
	for(int i=0;i<size;i++){
		cout<<" "<<array[i];
	}
}
int main(){
	//two sorted arrays
	int arr1[]={2,5,7,9};
	int arr2[]={1,3,4,6};
	int size1=sizeof(arr1)/sizeof(arr1[0]);
	int size2=sizeof(arr2)/sizeof(arr2[0]);
	int size3=size1+size2;
	int arr3[size3];
	int k=0,i=0,j=0;
	while(k<size3){
		if(arr1[i]<arr2[j]){
			arr3[k]=arr1[i];
			i++;
		}else{
			arr3[k]=arr2[j];
			j++;
		}
		k++;
	}
	while(i<size1){
		arr3[k]=arr1[i];
		i++;k++;
	}
	while(j<size2){
		arr3[k]=arr2[j];
		j++;
		k++;
	}
	print(arr3,size3);
}
