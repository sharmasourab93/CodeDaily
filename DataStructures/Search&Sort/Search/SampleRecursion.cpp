//Sample Recursion
#include<iostream>
using namespace std;
int r(int i){
	if(true){
		cout<<i<<endl;
		i++;
		r(i);
		i--;
		r(i);
	}
}
int main(){
	r(0);
}
