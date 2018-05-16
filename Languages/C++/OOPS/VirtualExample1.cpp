//Virtual Class Example
#include<iostream>
using namespace std;
class func1{
	public:
		virtual
		void show(){
			cout<<"In Func1::show()"<<endl;
		}
};
class func2: public func1{
	public:
		void show(){
			cout<<"In Func2::show()"<<endl;
		}
};
int main(){
	
	func2 f2;
	func1 &f1=f2;
	f1.show();
}
