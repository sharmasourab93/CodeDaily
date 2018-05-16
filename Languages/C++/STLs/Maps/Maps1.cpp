#include<bits/stdc++.h>
using namespace std;

int main(){
		map<int,int>g;
		
		g.insert(pair<int,int>(10,20));
		g.insert(pair<int,int>(20,40));
		g.insert(pair<int,int>(40,80));
		map<int,int>::iterator i;
		for(i=g.begin();i!=g.end();i++){
			cout<<i->first<<" "<<i->second<<endl;
		}
		
		i=g.find(10);
		g.erase(i);
		cout<<endl;
		for(i=g.begin();i!=g.end();i++){
			cout<<i->first<<" "<<i->second<<endl;
		}
		
}
