//ReferenceVsPointers
#include<iostream>
using namespace std;
int main(){
	int x=10;
	int &y=x;
	int *z=&x;
	cout<<"x= "<<&x<<endl;
	cout<<"&y= "<<y<<endl;
	cout<<"*z= "<<*z<<endl;
}
