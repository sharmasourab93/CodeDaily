//Reference to C is ambiguous
#include<iostream>
using namespace std;
class A{
	public:
		char c;
};
class B{
	public:
		int c;
};

class Derived:public A,public B{
	public:
		Derived(){
			cout<<c<<endl;
		}
};
int main(){
	Derived d;
}
