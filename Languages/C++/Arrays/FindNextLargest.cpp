//Finding two next number of larger number 
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
void swap(char *a,char *b){
	char temp=*a;
	*a=*b;
	*b=temp;
}
void findNext(char number[], int n){
	int i,j;
	for(i=n-1;i>0;i--){
		if(number[i]>number[i-1]) break;
	}
	//cout<<"\nFirst for loop"<<endl;
	if(i==0) {
		cout<<"Next is not possible"<<endl; 
		return;
	}
	int x=number[i-1], smallest=i;
	//cout<<"\nSecond for loop"<<endl;
	for(j=i+1;j<n;j++){
		if(number[j]>x&&number[j]<number[smallest])
			smallest=j;
	}
	swap(&number[smallest],&number[i-1]);
	//cout<<"\nSwapping"<<endl;
	sort(number+i,number+n);
	cout<<"The Next largest number is:"<<number;
}
int main(){
	char digits[]="534976";
	int n=strlen(digits);
	findNext(digits,n);
	
}
