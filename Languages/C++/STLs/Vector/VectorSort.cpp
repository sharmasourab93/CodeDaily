//Vector Sorting using STLS
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
int main(){
	vector<int> v;
	v.push_back(10);
	v.push_back(20);
	v.push_back(5);
	v.push_back(2);
	v.push_back(23);
	int size=v.size();
	vector<int>::iterator i;
	for(i=v.begin();i!=v.end();++i){
		cout<<*i<<" ";
	}
	cout<<"\nAfter Sorting:"<<endl;
	sort(v.begin(),v.end());
	for(i=v.begin();i!=v.end();++i){
		cout<<*i<<" ";
	}
	cout<<"\nAfter Reversing:"<<endl;
	reverse(v.begin(),v.end());
	for(i=v.begin();i!=v.end();++i){
		cout<<*i<<" ";
	}
}
