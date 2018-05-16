//Quick Sort
#include<iostream>
using namespace std;
class QuickSort{
	public:
	int swap(int *a, int *b){
		int t=*a;
		*a=*b;
		*b=*a;
		return (*a,*b);
	}
	int partition(int array[], int low,int high){
		cout<<"Partition"<<endl;
		int pivot=array[((high-low)/2)+1];
		int i=low-1;
		for(int j=0;j<=high-1;j++){
			cout<<"For Loop"<<endl;
			if(array[j]<=pivot){
				i++;
				swap(&array[i],&array[j]);	
			}
		}
		swap(&array[i+1],&array[high]);
		return(i+1);
	}
	void quickSort(int array[],int low, int high){
		if(low<high){
			int pi=partition(array,low,high);
			quickSort(array,low, pi-1);
			quickSort(array,pi+1,high);
		}
	}
	int printArray(int arr[],int size){
		int i;
		for(int i=0;i<size;i++){
			cout<<arr[i]<<" ";
		}
		cout<<endl;
	}
	int main1(){
		int arr[]={10,7,8,9,1,5};
		int n=sizeof(arr)/sizeof(arr[0]);
		cout<<"Quick Sort"<<endl;
		quickSort(arr,0,n-1);
		cout<<"\n Sorted Array: "<<endl;
		printArray(arr,n);
		return 0;
	}
};
int main(){
	QuickSort qs;
	qs.main1();
}
