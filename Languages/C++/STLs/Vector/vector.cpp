//Binary Search using STL 
#include<iostream>
#include<vector>
#include<algorithm>
#include<iterator>
using namespace std;
int main(){
	int arr[]={10,20,30,5,32,23,15};
	int n=sizeof(arr)/sizeof(arr[0]);
	vector<int> vect(arr,arr+n);
	vector<int>::iterator i;
	for(i=vect.begin();i!=vect.end();++i){
		cout<<*i<<" ";
	}

	
}
