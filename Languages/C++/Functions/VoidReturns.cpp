//Void function Exploration 
#include<iostream>
using namespace std;
int cantwork(){
	cout<<"I cannot work"<<endl;
	return;
}
void work(){
	cout<<"\nWork FUnction"<<endl;
	return cantwork();
}

int main(){
	work();
	return 0;
}
