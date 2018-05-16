/*Selection Sort*/
#include<iostream>
using namespace std;
class SelectionSort{
	public:
		void swap(int* a,int* b){
			int temp;
			temp=*a;
			*a=*b;
			*b=temp;
		}
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
		void printarr(int barr[], int m){
			for(int l=0;l<m;l++){
				cout<<"\t"<<barr[l];
			}
		}
		void exec(){
			int a[]={9,8,7,6,5,4,3};
			int size=((sizeof(a))/sizeof(a[0]));
			selectionSort(a,size);
		}
		
};
int main(){
	SelectionSort ss;
	ss.exec();
}
