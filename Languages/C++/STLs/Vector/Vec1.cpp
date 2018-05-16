#include<iostream>
#include<vector>
#include<iterator>
#define N 10
using namespace std;
int main(){
	vector<int> v1;
	vector<int>::iterator i;
	v1.push_back(10);
	v1.push_back(20);
	//v1.push_front(30);
	for(i=v1.begin();i!=v1.end();++i){
		cout<<*i<<" "<<endl;
	}
	cout<<v1.at(1);
	cout<<"\nFront "<<v1.front()<<endl;
	cout<<"\nBack "<<v1.back()<<endl;
	v1.assign(0,2);
	for(i=v1.begin();i!=v1.end();++i){
		cout<<*i<<" "<<endl;
	}
}
