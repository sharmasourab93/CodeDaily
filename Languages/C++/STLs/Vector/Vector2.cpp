#include<bits/stdc++.h>
using namespace std;

int main(){

	string line="Sourab Sampath Kumar Upadhya Sharma";

	vector<string> tokens;
	stringstream check1(line);
	string temp;
	while(getline(check1,temp,' ')){
		tokens.push_back(temp);
	}
	vector<string>::iterator i;
	cout<<"Vector size: "<<tokens.size()<<endl;
	cout<<"Vector address: "<<&tokens<<endl;
	for(i=tokens.begin();i!=tokens.end();i++){
		cout<<*i<<" "<< &*i<<endl;
	}
}
