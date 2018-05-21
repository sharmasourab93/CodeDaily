/*Insertion Sort*/
#include<iostream>
using namespace std;
//Function to swap 2 numbers
void swap(int * a, int* b){
	int temp;
	temp=*a;
	*a=*b;
	*b=temp;
}
//Insertion Sort Function
void insertionSort(int a[],int n){
	int i,j,min;
	for(i=1;i<n;i++){
		min=a[i];
		j=i-1;
		while(j>=0&&a[j]>min){
			a[j+1]=a[j];
			j--;
		}
		a[j+1]=min;
	}
}

//Bubble Sort
void bubble(int arr[], int n){
	for(int i=0;i<n;i++){
		cout<<"i "<<i<<endl;
		for(int j=0;j<n-i-1;j++){
			cout<<"\tj "<<j<<endl;
			if(arr[j]>arr[j+1]){
				swap(&arr[j],&arr[j+1]);
			}
		}
	}
	printarr(arr,n);
}

//Selection Sort
void selectionSort(int arr[],int n){
	int min;
	for(int i=0;i<n-1;i++){
		min=i;
		for(int j=i+1;j<n;j++)
			if(arr[j]<arr[min])
				min=j;
		swap(&arr[min],&arr[i]);
	}
	printarr(arr,n);
}

//Function to Keep the Tree Heapify or matching the condition
void heapify(int arr[],int n, int i){
	int largest=i;
	int l=2*i+1;
	int r=2*i+2;
	if(l<n && arr[l]>arr[largest]){
		largest=l;
	}
	if(r<n && arr[r]>arr[largest]){
		largest=r;
	}
	if(largest!=i){
		swap(&arr[i],&arr[largest]);
		heapify(arr,n,largest);
	}
}

//Function to sort the Heap
void heapsort(int arr[], int n){
	for(int i=n/2-1;i>=0;i--){
		heapify(arr,n,i);
	}
	for(int j=n-1;j>=0;j--){
		swap(&arr[0],&arr[j]);
		heapify(arr,j,0);
	}
}
//Prints an array
void printarr(int a[],int n){
	for(int l=0;l<n;l++){
		cout<<"\t"<<a[l];
	}
}
int main(){
	int a[]={10,9,8,1,6,5,4};
	int size=((sizeof(a))/sizeof(a[0]));
	insertionSort(a,size);
	printarr(a,size);
}

