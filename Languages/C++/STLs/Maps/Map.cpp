//Map 
#include<iostream>
#include<map>
#include<iterator>
using namespace std;
int main(){
	map<int,int> g1;
	g1.insert(pair <int,int>(1,40));
	g1.insert(pair <int,int>(2,30));
	g1.insert(pair <int,int>(3,60));
	g1.insert(pair <int,int>(4,20));
	g1.insert(pair <int,int>(7,10));
	
	map<int,int> ::iterator itr;
	for(itr=g1.begin();itr!=g1.end();++itr){
		cout<<itr->first<<" "<<itr->second<<endl;
	}
	cout<<endl;
	g1.erase(7);
	for(itr=g1.begin();itr!=g1.end();++itr){
		cout<<itr->first<<" "<<itr->second<<endl;
	}
	cout<<endl;
	map<int,int> g2(g1.begin(),g1.end());
	for(itr=g1.begin();itr!=g1.end();++itr){
		cout<<itr->first<<" "<<itr->second<<endl;
	}
	
}

