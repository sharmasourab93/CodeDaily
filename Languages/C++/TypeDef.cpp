#include<iostream>
#include<vector>
using namespace std;
int main(){
	typedef vector v1;
	v1 v(0,10);
	for(int i=0;i<10;i++){
		cout<<v[i]<<" ";
	}
	
}
