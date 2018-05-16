#include<iostream>
using namespace std;
int main(){
	float x=10.3;
	int y;
	y=int (x);
	cout<<y<<endl;
	char a='S';
	int b,c;
	b=(int)a;
	cout<<b<<endl;
	c=int (a);
	cout<<c<<endl;
	cout<<sizeof(double)<<" "<<sizeof(long)<<endl;
	return 0;
}
