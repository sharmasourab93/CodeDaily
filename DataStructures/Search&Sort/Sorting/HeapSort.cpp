/*Heap Sort Algorithm*/
//Min Heap
#include<iostream>
using namespace std;
class HeapSort{
	public:
		void swap(int * a, int * b){
			int temp;
			temp=*a;
			*a=*b;
			*b=temp;
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
		void printArray(int arr[], int n){
 		   	for (int i=0; i<n; ++i){
 		   			cout << arr[i] << " ";
    				cout << "\n";
				}
			}
		void exec(){
			int array[]={20,56,10,45,22,78,33};
			int s=((sizeof(array))/(sizeof(array[0])));
			heapsort(array,s);
			printArray(array,s);
		}
};
int main(){
	HeapSort HS;
	HS.exec();
}
