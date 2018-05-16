#include<iostream>
using namespace std;
int main(){
	mutable int i=10;
	int j=i+10;
	j++;


	//Works fine because we don't have to  increment a read only operator
	
}
