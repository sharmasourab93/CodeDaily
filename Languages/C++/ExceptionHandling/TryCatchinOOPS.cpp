#include<iostream>
using namespace std;
class Test{
	
	public:
	~Test(){
		cout<<"Destructing Test"<<endl;
	}
	public: 
	Test(){
		cout<<"Constructing Test"<<endl;
	}
};
int main(){
	try {
		Test t;
		throw t;
		
	}
	catch(...){
		cout<<"Caught Test object"<<endl;
	}
}
