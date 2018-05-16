//Merger Sort
#include<iostream>
using namespace std;
class MSort{
	public:
		void merge(int *array,int l,int m, int r);
		void mergesort(int *array,int low, int high);
		void printarray(int *array,int size){
			cout<<"\nPrinting Array:"<<endl;
			for(int i=0;i<size;i++){
				cout<<array[i]<<" ";
			}
		}
		void driver(){
			int array[]={10,23,12,9,65,78,66,98,11};
			int arr_size=((sizeof(array))/sizeof(array[0]));
			cout<<"\nBefore sorting the array:"<<endl;
			printarray(array,arr_size);
			mergesort(array,0,arr_size);
			cout<<"\nAfter sorting: "<<endl;
			printarray(array,arr_size);
		}		
};
int main(){
	MSort ms;
	ms.driver();
}
void MSort::mergesort(int *array,int l, int r){
	if(l<r){
		//Finding the middle element
		int m=l+(r-l)/2;
		//Sort first and second half
		mergesort(array,l,m);
		mergesort(array,m+1,r);
		//Calling on merge
		merge(array,l,m,r);
	}
}
void MSort::merge(int *array,int l, int m, int r){
	int i,j,k;
	int n1=m-l+1;
	int n2=r-m;
	
	int L[n1],R[n2];
	
	for(i=0;i<n1;i++)
		L[i]=array[l+i];
	for(j=0;j<n2;j++)
		R[j]=array[m+1+j];
		
	i=0;j=0;k=l;
	while(i<n1&&j<n2){
		if(L[i]<=R[j]){
			array[k]=L[i];
			i++;
		}else{
			array[k]=R[j];
			j++;
		}
		k++;
	}
	while(i<n1){
		array[k]=L[i];
		i++;
		k++;
	}
	while(j<n2){
		array[k]=R[j];
		j++;
		k++;
	}
}
