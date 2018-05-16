#include<iostream>
using namespace std;
template<typename X>
X returnSum(X x, X y){
	cout<<x+y;
}
int main(){
	returnSum(10.5,11.4);
}