#include<iostream>
#include<ctime>
using namespace std;
int main(){
	time_t x={time(0)};
	char *ct;
	ct=ctime(&x);
	cout<<"CT"<<ct;
}
