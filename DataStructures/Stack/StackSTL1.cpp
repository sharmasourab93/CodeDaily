//Stack using STLs
#include<iostream>
#include<stack>
using namespace std;
int main(){
	std::stack<int> s;
	s.push(21);
	s.push(22);
	s.push(23);
	cout<<s.top()<<endl;
	int *x=s.top();
	s.pop();
	delete(*x);
	cout<<s.top();
	if(s.empty()==1)
	cout<<s.top()<<endl;
	
}
