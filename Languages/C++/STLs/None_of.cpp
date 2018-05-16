//None_of
#include<iostream>
using namespace std;
int main(){
	int ar[6]={1,2,3,4,5,-6};
	none_of(ar,ar+6,[](int x){return x>0;})? cout<<"No negative elements":
	cout<<"All are negative elements";
	return 0;
}
