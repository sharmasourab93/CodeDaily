//Vector and iterator
#include<iostream>
#include<vector>
#include<iterator>
using namespace std;
int main(){
	vector<int> vect;
	vector<int>::iterator ptr;
	for(int i=1;i<=5;i++){
		vect.push_back(i);
	}
	cout<<"output of begin and end\t:\t";
	for(ptr=vect.begin();ptr!=vect.end();++ptr){
		cout<<*ptr<<'\t';
	}
	cout<<"\nSize "<<vect.size();
	cout<<"\nCapacity "<<vect.capacity();
	cout<<"\nMax Size "<<vect.max_size();
	cout<<"\nAt 3"<< vect.at(3);
	cout<<"\nfront "<<vect.front();
	cout<<"\nBack "<<vect.back();
	return 0;
	
}

