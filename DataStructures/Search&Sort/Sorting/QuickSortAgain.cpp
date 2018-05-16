//Quick Sort once again
#include<iostream>
using namespace std;
class Qsort{
	public:
		void swap(int *a,int *b){
			int temp=*a;
			*a=*b;
			*b=temp;
		}
		int partition(int *array,int low, int high);
		void quicksort(int *array,int low, int high);
		void printarray(int *array,int size);
		void driver();
};
int main(){
	Qsort s;
	s.driver();
}
int Qsort::partition(int *array,int low,int high){
	int pivot=array[high];
	int i=(low-1);
	for(int j=low;j<=high-1;j++){
		if(array[j]<=pivot){
			i++;
			swap(&array[i],&array[j]);
		}
	}
	swap(&array[i+1],&array[high]);
	return (i+1);
}
void Qsort::quicksort(int *array,int low,int high){
	if(low<high){
		int pi=partition(array,low,high);
		quicksort(array,low,pi-1);
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
