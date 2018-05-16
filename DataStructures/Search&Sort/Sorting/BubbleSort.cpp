/*Bubble Sort*/
#include<iostream>
using namespace std;
class BubbleSort{
	public:
		void swap(int *a,int *b){
			int temp;
			temp=*a;
			*a=*b;
			*b=temp;
		}
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
		void printarr(int barr[], int m){
			for(int l=0;l<m;l++){
				cout<<"\t"<<barr[l];
			}
		}
		void exec(){
			int a[]={9,8,7,6,5,4,3};
			int size=((sizeof(a))/sizeof(a[0]));
			bubble(a,size);
		}
};
int main(){
	BubbleSort bs;
	bs.exec();
}
