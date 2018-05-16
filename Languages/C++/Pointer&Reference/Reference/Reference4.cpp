#include<iostream>
using namespace std;
int main(){
	int x=5;
	int *ptr=&x;
	int &ref=*ptr;
	cout<<ref;
}
