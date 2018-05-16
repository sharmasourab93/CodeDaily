#include<iostream>
using namespace std;
int main(){
	char a='A';
	char b='B';
	//Using Const char *
	//Cannot change the value of the pointer but can change the value
	//Mutable pointer to an immutable variable
	
	const char *ptr=&a;
	cout<<*ptr<<" "<<&ptr<<endl;
	ptr=&b;
	cout<<*ptr<<" "<<&ptr<<endl;
	
	//Using char *const
	//Immutable pointer ,content mutable
	/*
	char *const ptr=&a;
	cout<<*ptr<<" "<<&ptr<<endl;
	//Below statement illegal
	//ptr=&b;
	*/
	//Immutable pointer to an immutable variable
	const char *const ptr=&a;
	cout<<*ptr<<" "<<&ptr<<endl;
	
	//ptr=&b;
	cout<<*ptr<<" "<<&ptr<<endl;
	
}
