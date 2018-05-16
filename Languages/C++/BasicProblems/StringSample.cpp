#include<iostream>
#include<string.h>
using namespace std;
void swap(char *a,char *b){
	char t=*a;
	*a=*b;
	*b=*a;
}
void reverse(string x,int len){
	int j=len-1;
	for(int i=0;i<len/2;i++){
		if(j>len/2-1){
			swap(x[i],x[j]);
			j--;
		}
	}
	cout<<x<<endl;
}
int main(){
	int x=7/3;
	cout<<x<<endl;
	string s="sourab";
	int len=s.length();
	reverse(s,len);
}
