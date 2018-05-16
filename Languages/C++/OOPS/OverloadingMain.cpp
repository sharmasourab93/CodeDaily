#include<iostream>
using namespace std;
int main(){
	static int m;
	cout<<m++<<endl;
	main();
}
