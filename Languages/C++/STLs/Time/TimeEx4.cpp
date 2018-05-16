#include<iostream>
#include<ctime>
using namespace std;
int main(){
	time_t now=time(0);
	cout<<"The time since Jan 1,1970"<<now<<endl;
	tm *lm=localtime(&now);
	cout<<"Year"<<1900+lm->tm_year<<endl;
	cout<<"Month"<<lm->tm_mon<<endl;
	cout<<"Day"<<lm->tm_mday<<endl;
	cout<<__TIME__;
	
}
