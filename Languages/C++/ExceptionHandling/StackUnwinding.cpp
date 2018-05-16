#include<iostream>
using namespace std;
void f1() throw(int){
	cout<<"f1() starts"<<endl;
	throw 100;
}
void f2(){
	cout<<"f2 starts"<<endl;
	try{
		f1();	
	}
	catch(int x){
		cout<<"Catching Integer Exception"<<endl;
	}
	cout<<"f2() ends"<<endl;
}
int main(){
	f2();
}
