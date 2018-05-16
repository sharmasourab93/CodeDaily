#include<iostream>
#include<vector>
#include<map>
using namespace std;
int main(){
	typedef vector<int> v;
	v vec;
	vec.push_back(10);
	v::iterator j;
	for(j=vec.begin();j!=vec.end();++j){
		cout<<*j<<" ";
	}
	map<int,int> m;
	m.insert(pair<int,int>(10,20));
	map<int,int>::iterator i;
	for(i=m.begin();i!=m.end();++i){
		cout<<i->first<<endl;
		cout<<i->second<<endl;
	}
	
}
