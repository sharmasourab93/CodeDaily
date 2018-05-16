//Templates
//Class Templates
#include<iostream>
using namespace std;
template <typename X>
X returnMax(X x,X y){
	return (x>y)?x:y;
}
int main(){
	cout<<returnMax(4,3)<<endl;
	cout<<returnMax(5.2,6.4)<<endl;
}
