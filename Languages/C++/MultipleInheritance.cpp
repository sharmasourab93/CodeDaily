//Diamond Problem 2
#include<iostream>
using namespace std;
class B{
	public: B(){
		cout<<"B's constructor called"<<endl;
	}
};

class A{
	public: A(){
		cout<<"A's constructor called"<<endl;
	}
};

class C:public B,public A{
	public:
		C(){
			cout<<"C's Constructor called"<<endl;
		}
};
int main(){
	C c;
	
}
