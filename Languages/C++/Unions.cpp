#include<iostream>
using namespace std;

union test1{
	char y;
	int z;
}t1;
int main(){

	// When Changes are first made to t1.y

	t1.y='a';
	cout<<"Size of t1 after assigning value to y: "<<sizeof(t1)<<endl;
	/*cout<<"t1.x-->"<<t1.x<<" "*/cout<<t1.y<<"<-- t1.y "<<"   t1.z "<<t1.z<<endl;
	cout<<"&t1 "<<&t1<<endl;
	/*cout<<"&t1.x "<<&t1.x*/cout<<" &t1.y "<<&t1.y<<" &t1.z "<<&t1.z<<endl;
	cout<<endl;
cout<<sizeof(float)<<endl;
	//t1.x=5;

	cout<<"Size of t1 after changing the value of x: "<<sizeof(t1)<<endl;
	/*cout<<"t1.x-->"<<t1.x*/cout<<" "<<t1.y<<"<-- t1.y "<<" t1.z "<<t1.z<<endl;
	cout<<"&t1 "<<&t1<<endl;

}