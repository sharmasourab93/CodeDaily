#include<iostream>
using namespace std;
int sort(int array[], int n){
	int i,j,min;
	for(i=1;i<n;i++){
		min=array[i];
		j=i-1;
		while(j<n&&array[j]>min){
			array[j+1]=array[j];
			j++;
		}
		array[j]=min;
	}
}
int main(){
	int array[]={10,1,3,45,67,8,9};
	int x=11;
	int l=0,r=((sizeof(array))/(sizeof(array[0])))-1;
	sort(array,r);
	while(l<r){
		if(array[l]+array[r]==x){
			cout<<l<<" "<<r<<endl;return 1;	
		}
		else if(array[l]+array[r]<x) {
			l++;
		}
		else if(array[l]+array[r]>x){
			r--;	
		}  
		else return 0;
	}
}
