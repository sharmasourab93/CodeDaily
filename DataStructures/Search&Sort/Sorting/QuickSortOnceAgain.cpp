//Quick Sort on different cases
#include<iostream>
using namespace std;
class Qsort{
	public:
		void swap(int *a,int *b){
			int temp=*a;
			*a=*b;
			*b=temp;
		}
		int partition(int *array,int low, int high,int pivot);
		void quicksort(int *array,int low, int high);
		void printarray(int *array,int size);
		void driver();
};
int main(){
	Qsort s;
	s.driver();
}
int Qsort::partition(int *array, int low, int high,int pivot){
	int i=low-1;
	while(low<=high){
		while(array[low]<=pivot){
			low++;
		}
		while(array[high]>=pivot){
			high++;
		}
		if(low<=high){
			swap(&array[low],&array[high]);
			low++;
			high--;
		}
	}
	return low+1;
}
void Qsort::quicksort(int *array,int low,int high){
	if(low<high){
		int pivot=array[(low+high)/2];
		int pi=partition(array,low,high,pivot);
		quicksort(array,low,pi);
		quicksort(array,pi+1,high);
	}
}
void Qsort::printarray(int *array,int size){
	cout<<"\nPrinting Array:"<<endl;
	for(int i=0;i<size;i++){
		cout<<array[i]<<" ";
	}
}
void Qsort::driver(){
	int array[]={10,23,12,9,65,78,66,98,11};
	int arr_size=((sizeof(array))/sizeof(array[0]));
	cout<<"\nBefore sorting the array:"<<endl;
	printarray(array,arr_size);
	quicksort(array,0,arr_size);
	cout<<"\nAfter sorting: "<<endl;
	printarray(array,arr_size);
}
