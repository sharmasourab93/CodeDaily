//Set data structure
#include<iostream>
#include<set>
#include<iterator>
using namespace std;
int main(){
	set<int> g1;
	g1.insert(40);
	g1.insert(25);
	g1.insert(60);
	g1.insert(20);
	g1.insert(50);
	
	set <int>::iterator itr;
	cout<<"\n The set g1 is "<<endl;
	for(itr=g1.begin();itr!=g1.end();++itr){
		cout<<'\t'<<*itr;
	}
	cout<<endl;
	set <int> g2(g1.begin(),g1.end());
	for(itr=g2.begin();itr!=g2.end();++itr){
		cout<<'\t'<<*itr;
	}
	cout<<endl<<*g1.lower_bound(30)<<endl;
	cout<<endl<<*g2.upper_bound(30)<<endl;
	
	return 0;	
}
