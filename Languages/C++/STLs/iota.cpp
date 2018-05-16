//Iota
#include<iostream>
#include<algorithm>
#include<numeric>
#include<iota>
using namespace std;
int main(){
	int ar[6]={0};
	//Using iota() to assing values
	iota(ar,ar+6,20);
	//Displaying the new array
	cout<<"the new array after assinging values is:";
	for(int i=0;i<6;i++){
		cout<<ar[i]<<" ";
	}
	return 0;
}
