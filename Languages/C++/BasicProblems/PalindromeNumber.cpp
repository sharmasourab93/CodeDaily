//Palindrome Number
#include<iostream>
using namespace std;
int main(){
	int n=1001;
	int temp=n;
	int reverse;
	while(temp!=0){
		reverse=reverse*10;
		reverse=reverse+(temp%10);
		temp=temp/10;
	}
	if(n==reverse){
		cout<<" Is a palindrome"<<endl;
	}else{
		cout<<"Not a palindrome"<<endl;
	}
}
