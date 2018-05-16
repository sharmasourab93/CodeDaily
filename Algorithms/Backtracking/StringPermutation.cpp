//Permutations of a string 
#include<iostream>
#include<string>
using namespace std;
void permute(char s[],int f,int size);
int main(){
	char s[]="ABC";
	int len=((sizeof(s))/(sizeof(s[0])));
	permute(s,0,len-1);
}
void swap(char *a, char *b){
	char t;
	 t=*a;
	*a=*b;
	*b=t;
}
//A utility function which permutates and prints a string
void permute(char *s,int f,int n){
	int i;
	int len=((sizeof(s))/(sizeof(s[0])));
	if(f==n){
		cout<<s<<endl;
	}else{
		for(i=f;i<=n;i++){
			swap((s+f),(s+i));
			permute(s,f+1,n);
			swap((s+f),(s+i));
		}
	}
}
