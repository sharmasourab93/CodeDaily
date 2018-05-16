//Priority Queue
#include<iostream>
#include<queue>
using namespace std;
int main(){
	priority_queue<int> g;
	g.push(10);
	g.push(20);
	g.push(30);
	g.push(40);
	g.push(50);
	
	cout<<" Size"<<g.size();
	cout<<" Top "<<g.top();
}
