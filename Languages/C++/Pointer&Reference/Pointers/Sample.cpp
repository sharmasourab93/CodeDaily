#include<iostream>
using namespace std;
int main(){
	int *a=new int[10];
	a[0]=1;
	a[1]=2;
	cout<<*(a+2);
}
