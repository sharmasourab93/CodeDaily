#include<iostream>
using namespace std;
int main(){
	struct x{
		char a;
		char gap;
		int b;
		char c;
		char d;
	}A;
	cout<<sizeof(A)<<endl;//gives 12 bytes
}
