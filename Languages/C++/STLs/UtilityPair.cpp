//Pair 
#include<iostream>
#include<utility>
using namespace std;
int main(){
	pair<string,string> PAIR("Geeky", "Sourab");
	cout<<PAIR.first<<endl;
	pair<string,string> PAIR1;
	PAIR1=make_pair("Sharma","sobby");
	cout<<PAIR1.first<<" "<<PAIR1.second<<endl;
	//PAIR1.swap(PAIR); //Will not work
	//cout<<"After swapping "<<PAIR1.first<<" "<<PAIR1.second;
	
	
}
