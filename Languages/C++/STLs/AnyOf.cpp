//any_of()
#include<iostream>
using namespace std;
int main(){
	int ar[6]={1,2,3,4,5,-6};
	any_of(ar,ar+6,[](int x){return x>0;})? cout<<"There exists a negative element":
	cout<<"All are positive elements";
	return 0;
}
