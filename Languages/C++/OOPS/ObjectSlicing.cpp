#include<iostream>
using namespace std;

class Base{
	int x,y;
};
class Derived: public Base{int z,a;};
//Can be overcome using & or *
int main(){
	Derived d;
	Base b=d;
	//cout<<b.z<<endl; //Prints that no such objects have been declared.
}