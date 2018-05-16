//MergeSort OVer again
#include<iostream>
using namespace std;
class Msort{
	public:
		void merge(int *array,int low,int mid,int high);
		void mergesort(int *array, int low, int high);
		void printarray(int *array, int size);
		void driver();
};
void Msort::driver(){
	int array[]={10,23,12,9,65,78,66,98,11};
	int arr_size=((sizeof(array))/sizeof(array[0]));
	cout<<"\nArray before sort:"<<endl;
	printarray(array,arr_size);
	cout<<"\nCalling Merge Sort:"<<endl;
	mergesort(array,0,arr_size);
	cout<<"Array after sort: "<<endl;
	printarray(array,arr_size);
	mergesort(array,0,arr_size);
	cout<<"Array after sort: "<<endl;
	printarray(array,arr_size);
}
void Msort::mergesort(int *array, int low, int high){
	if(low<high){
		int mid=(low+(high-low)/2);
		mergesort(array,low,mid);
		mergesort(array,mid+1,high);
		merge(array,low,mid,high);
	}
}
void Msort::merge(int *array,int low, int mid,int high){
	int i,j,k;
	int n1=mid-low+1;
	int n2=high-mid;
	int L[n1],R[n2];
	for(i=0;i<n1;i++){
		L[i]=array[low+i];
	}
	for(j=0;j<n2;j++){
		R[j]=array[mid+1+j];
	}
	i=0;
	j=0;
	k=low;
	while(i<n1&&j<n2){
		if(L[i]<=R[j]){
			array[k]=L[i];
			i++;
		}
		else{
			array[k]=R[j];
			j++;
		}
		k++;
	}
	while(i<n1){
		array[k]=L[i];
		i++;k++;
	}
	while(j<n2){
		array[k]=R[j];
		j++;k++;
	}
}
void Msort::printarray(int array[], int size){
	for(int i=0;i<size;i++){
		cout<<array[i]<<" ";
	}
}
int main(){
	Msort ms;
	ms.driver();
}
