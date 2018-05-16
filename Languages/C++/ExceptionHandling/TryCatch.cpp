//Basic Try Catch Example
#include<iostream>
using namespace std;
int main(){
	try{
		throw 'a';
	}
	catch (char x){
		cout<<"Caught character Exception"<<endl;
	}
}
