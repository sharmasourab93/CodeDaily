#include<iostream>
using namespace std;
class A{
	public:
		A(){
			cout<<"A class called "<<endl;
			cout<<this<<endl;
		}
		~A(){
			cout<<this<<endl;
			cout<<"A class terminated"<<endl;
		}
};
int main(){
	A a,b,c;
}
