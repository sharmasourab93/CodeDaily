#include<iostream>
using namespace std;
void xc(int *pu, int * xu){
	*pu=0;
	*xu=0;
	cout<<*pu<<" "<<*xu<<endl;
}
int main(){
	static int i;
	cout<<"i "<<i<<endl;
	i=2;
	int j=2;
	cout<<i<<" "<<j<<endl;
	xc(&i,&j);
	cout<<i<<" "<<j<<endl;
	
}
