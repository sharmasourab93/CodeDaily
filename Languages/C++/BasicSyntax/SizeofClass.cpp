#include<iostream>
using namespace std;
class Empty{
	
};
int main(){
	Empty t,u;
	cout<<sizeof(t)<<endl;
	cout<<sizeof(u)<<endl;
	if(&t==&u){
		cout<<"Same";
	}
}
