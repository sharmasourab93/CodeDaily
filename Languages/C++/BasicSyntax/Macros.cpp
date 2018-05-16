//Macros
#include<iostream>
#include <string.h>
using namespace std;
#define MIN(a,b) ((a<b)?a:b)
#define MAX(a,b) ((a>b)? a:b)
#define CONCAT(x,y) x##y
int main(){
	int a=0,b=1;
	//int ab=90;
	//cout<<CONCAT(a,b)<<endl;
	int c=MIN(a,b);
	int d=MAX(a,b);
	cout<<"C: "<<c;
	cout<<"D: "<<d<<endl;
   	string ti=__TIME__;
   	string xi=CONCAT(t,i);
   	string da=__DATE__;
   	string yi=CONCAT(d,a);
    string zi=CONCAT(CONCAT(x,i),CONCAT(y,i));
}
