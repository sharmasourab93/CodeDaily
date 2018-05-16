//Exception Handling 
#include<iostream>
using namespace std;
int main(){
	int x=-1;
	//Some code
	cout<<"Before Try\n";
	try{
		cout<<"Inside Try";
		if(x<0){
			throw x;
			cout<<"After Throw (never executed)\n";
		}
	}
	catch(int x){
		cout<<"Exception Caught\n";
	}
	cout<<"After catch";
	return 0;
}
