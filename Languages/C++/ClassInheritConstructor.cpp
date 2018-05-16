#include<iostream>
using namespace std;

class A{
public:
	A(){
		cout<<"\nA"<<endl;
	}
};
class B:public A{
public:
	B(){
		cout<<"\nB"<<endl;
	}
};

int main(){
	A a;
	B b;

}