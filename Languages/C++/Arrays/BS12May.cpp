//Binary Search 
#include<iostream>
#define N 10
using namespace std;
static int i;
int bsearch(int array[],int m,int n, int key){
	int mid=(m+n)/2;
	if(array[mid]<key){
		i++;
		int res=bsearch(array,mid+1,n,key);
	}else if(array[mid]>key){
		i++;
		int res=bsearch(array,m,mid,key);
	}else if(array[mid]==key){
		cout<<"Found at : "<<mid+1<<"th element"<<"\n Counter i: "<<i<<endl;
		return mid;
	}else{
		return -1;
	}
}
int swap(int *a,int *b){
	int temp=*a;
	*a=*b;
	*b=*a;
	return *a,*b;
}
void printarray(int *array){
	cout<<"\nPrinting array: "<<endl;
	for(int i=0;i<N;i++) cout<<array[i]<<" ";
}
int insertionSort(int *array){
	int i,j;
	for(i=1;i<N;i++){
		int key=array[i];
		j=i-1;
		while(j>=0&& array[j]>key){
			array[j+1]=array[j];
			j--;
		}
		array[j+1]=key;
	}
	return *array;
}
int insertSort(int *array,int n,int key){
	int i,j;
	printarray(array);
	for(i=n-1;(array[i]>key&& i<=0);i--){
		array[i+1]=array[i];
	}
	array[i]=key;
	return n+1;
	//For using inserttion array
	//*array=insertionSort(array);
}
int main(){
	int array[N]={3,6,8,10,12,45,78,88};
	int key=35;
	int n=8;
	n=insertSort(array,n,key);
	printarray(array);
	//int result=bsearch(array,0,size,key);
}
