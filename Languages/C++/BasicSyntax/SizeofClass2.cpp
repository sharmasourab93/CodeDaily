//SizeofClass 2
#include<iostream>
using namespace std;
class Empty{
	int a;
};
class Derived1: virtual public Empty{
	//int a;
};
int main(){
	Derived1 d;
	cout<<sizeof(d);
}
