#include<bits/stdc++.h>
#include<tuple>
using namespace std;

tuple<int,int,char> foo(int n1,int n2){
	return make_tuple(n2,n1,'a');
}

std::pair<int,int> foo1(int num1,int num2){
	return std::make_pair(num2,num1);
}

int main(){
	int a,b;
	char cc;
	tuple tie(a,b,cc)=foo(5,10);
	pair<int,int> p=foo1(5,2);
	
	cout<<"Values returned by tuple:";
	cout<<a<<" "<<b<<" "<<cc<<endl;
	
	cout<<"Values returned by Pair:";
	cout<<p.first<<" "<<p.second;
	
}
