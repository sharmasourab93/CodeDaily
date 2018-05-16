#include<iostream>
#include<queue>
using namespace std;
int main(){
	queue <int> gquiz;
	gquiz.push(10);
	gquiz.push(20);
	cout<<gquiz.back();
	cout<<" The queue gquiz is :";
	while(!gquiz.empty()){
		cout<<'\t'<<gquiz.front();
		gquiz.pop();
	}
	cout<<'\n';
	gquiz.push(10);
	gquiz.push(20);
	cout<<"\nSize "<<gquiz.size();
	cout<<"\nFront "<<gquiz.front();
	cout<<"\n Back "<<gquiz.back();
	
	//cout<<"\npop"<<gquiz.pop();
	return 0;
}
