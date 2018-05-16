//Union & Intersection to Two sorted arrays
#include<iostream>
using namespace std;
void printarray(int *array,int size){
	for(int i=0;i<size;i++){
		cout<<array[i]<<" ";
	}
}
void unionset(int *a1,int s1,int *a2,int s2){
	int i=0,j=0;
	while(i<s1&&j<s2){
		if(a1[i]<a2[j]){
			cout<<a1[i]<<" ";
			i++;
		}else if (a1[i]>a2[j]){
			cout<<a2[j]<<" ";
			j++;
		}else if (a1[i]==a2[j]){
			cout<<a1[i]<<" ";
			i++;j++;
		}
	}
		while(i<s1){
			cout<<a1[i++]<<" ";
		}
		while(j<s2){
			cout<<a2[j++]<<" ";j++;
		}
	cout<<endl;
}
void intersection(int *a1,int s1,int *a2,int s2){
	int i=0,j=0;
	while(i<s1&&j<s2){
		if(a1[i]<a2[j]){
			i++;
		}if(a1[i]>a2[j]){
			j++;
		}else if(a1[i]==a2[j]){
			cout<<a1[i]<<" ";
			i++;j++;
		}
	}
}
int main(){
	int array1[]={1,3,4,5,7};
	int size1=sizeof(array1)/sizeof(array1[0]);
	int array2[]={2,3,5,6};
	int size2=sizeof(array2)/sizeof(array2[0]);
	unionset(array1,size1,array2,size2);
	intersection(array1,size1,array2,size2);
}
