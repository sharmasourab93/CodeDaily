//Number occuring Odd number of times 
#include<iostream>
using namespace std;
//O(n) solution using Bitwise XOR Operator
int getOddOccurence(int *arr, int size){
	int i;
	int res=0;
	for(i=0;i<size;i++){
		res=res^arr[i];
	}
	return res;
}
//O(n^2) solution
/*int getOddOccurence(int *arr, int size){
	int i,j;
	int max=0;
	int count;
	int number, num;
	for(i=0;i<size;i++){
		count=0;number=arr[i];
		for(j=0;j<size;j++){
			if(arr[i]==arr[j]){
				count++;
			}
		}
		if(count>max&&count%2==1){
			max=count;
			num=number;
			cout<<max<<" "<<num<<endl;
		}
	}
	return num;
}*/
int main(){
	int arr[]={2,3,5,4,5,2,4,3,5,2,4,4,2};
	int n=sizeof(arr)/sizeof(arr[0]);
	cout<<getOddOccurence(arr,n);
}
