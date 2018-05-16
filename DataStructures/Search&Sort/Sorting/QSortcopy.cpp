//Quick Sort 
#include<iostream>
using namespace std;
class QSort{
	public:
		int swap(int *a,int *b){
			int temp=*a;
			*a=*b;
			*b=temp;
			return *a,*b;
		}
		int partition(int *array,int low, int high);
		void quicksort(int *array, int low, int high);
		void printarray(int *array, int size);
		void driver();
};
void QSort::driver(){
	int array[]={10,23,12,9,65,78,66,98,11};
	int arr_size=((sizeof(array))/sizeof(array[0]));
	
	cout<<"\nBefore Sorting:"<<endl;
	printarray(array,arr_size);
	cout<<"Calling Sort:"<<endl;
	quicksort(array,0,arr_size-1);
	cout<<"\nAfter calling sort: "<<endl;
	printarray(array,arr_size);
	
}
void QSort::printarray(int *array, int size){
	for(int i=0;i<size;i++){
		cout<<array[i]<<" ";
	}
}
void QSort::quicksort(int *array,int low, int high){
	if(low<high){
		int pi=partition(array,low,high);
		quicksort(array,low,pi-1);
		quicksort(array,pi,high);
	}
}
int QSort::partition(int *array,int low,int high){
	int pivot=array[high];
	int i=low;
	for(int j=low;j<high;j++){
		//If current element is smaller than or 
		//equal to pivot
		if(array[j]<=pivot){
			i++;	//Incrementing index of smaller elements
			swap(&array[i],&array[j]);
		}
	}
	swap(&array[i+1],&array[high]);
	return(i+1);
}
int main(){
	QSort qs;
	qs.driver();
}
