//Print Leaders
#include<iostream>
using namespace std;
int main(){
	int array[]={16,17,4,3,5,2};
	int size=sizeof(array)/sizeof(array[0]);
	int max=array[size-1];
	cout<<max<<" ";
	for(int i=size-1;i>=0;i--){
		if(max<array[i]){
			max=array[i];
			cout<<max<<" ";
		}
	}
	cout<<endl;
}
