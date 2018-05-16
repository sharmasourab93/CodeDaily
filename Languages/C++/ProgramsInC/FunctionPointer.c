//Function pointer
#include<stdio.h>
int add(int a , int b){
	int c=a+b;	
	printf("\n%d",c);
	return(c);
}
int main(){
	int a=10,b=20;
	int c;
	void (*p)(int,int)=add;//Assinging the pointer function to the declared function 
	p(a,b);//passing arguments
}
