#include<iostream>
#include<stack>
#include<iomanip>
using namespace std;
int main(){
	std::stack<int> s;
	for(int i=0;i<10;i++){
		s.push(i);
	}
	int x=s.size();
	cout<<"Size: "<<x<<endl;
	stack<int>::iterator iter;
	for(iter=s.begin();iter!=iter.end();++i){
		cout<<*iter<<" ";
	}
	while(s.empty()){
		cout<<s.top()<<" ";
		s.pop();
	}
}
