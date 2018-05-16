//Shallow Copy & Deep Copy
#include<iostream>
using namespace std;
class C1{
public:
	int x;
	C1(){
		cout<<"Hello C1 "<<x<<" "<<endl;
	}
	C1(int x){
		this->x=x;
		cout<<" Hello C1 again "<<x<<endl;
	}
	~C1(){
		cout<<"Quiting C1 with value "<<x<<endl;
	}
	C1(const C1 &obj){this->x=15;C1();}
	int getX(){ return x;}
};

int main(){
	C1 c1,c2;
	c2=c1;
	cout<<&c1<<" "<<sizeof(c1)<<endl;
	cout<<&c2<<" "<<sizeof(c2)<<endl;
	cout<<c1.x<<" "<<c2.x<<endl;
	cout<<c1.getX()<<" "<<c2.getX()<<endl;
	c1.x=500;
	cout<<c2.x;
	
}

