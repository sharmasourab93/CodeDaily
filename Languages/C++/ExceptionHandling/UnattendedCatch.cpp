//Un attended Try Catch
#include<iostream>
using namespace std;
int main(){
	try{
		throw 'a';
	}
	catch (int x){
		cout<<"Caught integer Exception"<<endl;
	}
}
