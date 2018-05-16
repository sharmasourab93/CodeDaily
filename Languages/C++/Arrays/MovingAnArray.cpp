//Moving an array
#include<iostream>
using namespace std;
void printarray(int *array,int size){
	for(int i=0;i<size;i++){
		cout<<array[i]<<" ";
	}
	cout<<endl;
}
void swap(int *a,int *b){
	int temp=*a;
	*a=*b;
	*b=temp;
}
void rightrotate(int *array,int size,int rt){
	int temp[rt];
	for(int i=0;i<rt;i++){
		temp[i]=array[i];
	}
	for(int j=0;j<size-rt;j++){
		array[j]=array[j+rt];
	}
	int k=0;
	while(k<rt){
		array[size-rt+k]=temp[k];
		k++;
	}
	printarray(array,size);
}
void leftrotate(int *array,int size,int rt){
	int i,temp;
	temp=array[0];
	for(i=0;i<size-1;i++){
		array[i]=array[i+1];
	}
	array[i]=temp;
	printarray(array,size);
}
int main(){
	int array[]={10,11,12,13,14,15};
	int size=sizeof(array)/sizeof(array[0]);
	rightrotate(array,size,3);
	leftrotate(array,size,1);
	//justRotate(array,0,size);
}
