#include<iostream>
#include<ctime>
using namespace std;
int main(){
	int i;
	//Current date and time based on current system
	time_t now=time(0);
	//convert now to string form
	char* dt=ctime(&now);
	cout<<"the Locall date and time is"<<dt<<endl;
}
