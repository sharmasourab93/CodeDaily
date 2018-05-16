#include<iostream>
using namespace std;
int &fun(){
	static int x=10;
	return x;
}
int main(){
	cout<<fun();
	fun()=30;
	cout<<fun();
	return 0;
}
