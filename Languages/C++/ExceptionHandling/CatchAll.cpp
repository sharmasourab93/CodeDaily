//Catch All 
#include<iostream>
using namespace std;
int main(){
	try{
		throw 'a';
	}
	catch(...){
		cout<<"Caught"<<endl;
	}
}
