//Using this operator
#include<iostream>
using namespace std;
class Test{
		int a;
	public:
		int b;
		Test();
		void fun(int,int);
		Test(int x){
			b=x;
		}
};
Test::Test(){
	a=10;
}
void Test::fun(int a,int b){
	cout<<"\nthis->a "<<this->a<<endl;
	cout<<"Printing a from the argument "<<a<<endl;
	cout<<"this->b "<<this->b<<endl;
	cout<<"Printing b "<<b<<endl;
	Test(b);
	cout<<"this->b "<<this->b<<endl;
	cout<<"Printing b "<<b<<endl;
	
}
int main(){
	Test t;
	int k=4;
	t.fun(k,20);	
}
