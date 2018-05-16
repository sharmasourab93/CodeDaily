//Jump Search 
#include<iostream>
#include<cmath>
using namespace std;
int JumpSearch(int arr[], int x){
	int n=(sizeof(arr)/sizeof(arr[0]));
	int step=;
}
int main(){
	int arr[]={0,1,1,2,3,5,6,13,21,34,55,89,144,233,377,610};
	int x=89;
	int index=JumpSearch(arr,x);
	cout<<"Number is "<<x<<" and the index found is "<<index<<endl;
}
