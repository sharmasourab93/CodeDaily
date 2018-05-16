#include<iostream>
#include<deque>
using namespace std;
int main(){
	deque<int> dq;
	dq.push_back(10);
	dq.push_front(20);
	dq.push_back(30);
	dq.push_back(40);
	dq.push_back(50);
	deque<int>::iterator it;
	for(it=dq.begin();it!=dq.end();++it){
		cout<<" "<<*it;
	}
	cout<<endl;
	cout<<" Size of deque"<<dq.size()<<endl;
	cout<<" Max size"<<dq.max_size()<<endl;
	cout<<"At position 2"<<dq.at(2)<<endl;
	cout<<"Front "<<dq.front()<<endl;
	cout<<"back "<<dq.back()<<endl;
	
}
