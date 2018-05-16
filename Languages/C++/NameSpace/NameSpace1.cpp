//Namespaces in C++
#include<iostream>
using namespace std;
namespace first_func{
	void func(){
		cout<<"\nFunk Me!";
	}
}
namespace second_func{
	void func(){
		cout<<"\nDont Funk Me! But Fuck Me!";
	}
}
int main(){
	cout<<"\nUsing first Namespace";
	using namespace first_func;
	first_func::func();
	cout<<"\nUsing Second Namespace";
	using namespace second_func;
	second_func::func();
}
