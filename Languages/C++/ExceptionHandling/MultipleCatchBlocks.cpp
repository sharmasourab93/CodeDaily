//Multiple Catch Blocks 
#include<iostream>
using namespace std;
int main(){
	try{
		throw 'a';
	}
	catch (int x){
		cout<<"Caught integer Exception"<<endl;
	}
	catch(char x){
		cout<<" Caught character exception"<<endl;
	}
}
