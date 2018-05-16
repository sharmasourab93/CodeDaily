//Insertion sort 
#include<iostream>
using namespace std;
int insertionSort(int *array,int n){
	for(int i=1;i<n;i++){
		int key=array[i];
		int j=i-1;
		while(j>=0&&array[j]>key){
			array[j+1]=array[j];
			j--;
		}
		array[j+1]=key;
	}
	return *array;
}
void printarray(int *array, int n){
	for(int i=0;i<n;i++){
		cout<<array[i]<<" ";
	}
}
int main(){
	int array[]={98,12,34,56,67,88,45};
	int n=7;
	*array=insertionSort(array,7);
	printarray(array,7);
	
}
