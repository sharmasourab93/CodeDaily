//Making use of pair
#include<bits/stdc++.h>
#include<utility>
using namespace std;
int main(){
	pair<int,char> PAIR1;
	//cout<<PAIR1.first_type<<endl;
	PAIR1.first=100;
	PAIR1.second='G';
	cout<<PAIR1.first<<" "<<PAIR1.second<<endl;
	pair<int,string> g1=make_pair(1,"Sourab");
	pair<pair<int,char>,int> g2=make_pair(g1,120);
	cout<<g1.first<<" "<<g1.second<<endl;
	cout<<g2.first<<" "<<g2.second<<endl;
}
