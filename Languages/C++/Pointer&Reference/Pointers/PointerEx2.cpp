#include<stdio.h>
//using namespace std;
int main(){
	int a=5;
	int *p;
	p=&a;
	int **q;
	q=&p;
	int*** r;
	r=&q;
	printf("the value of a :%d",&a);
	printf("\nthe value of *p :%d",*p);
	printf("\nthe value of &p :%d",&p);
	printf("\nthe value of p :%d",p);	
	printf("\nthe value of q :%d",q);
	printf("\nthe value of *q :%d",*q);
	printf("\nthe value of **q :%d",**q);
	printf("\nthe value of r :%d",r);
	printf("\nthe value of *r :%d",*r);
	printf("\nthe value of **r :%d",**r);
	printf("\nthe value of ***r :%d",***r);
	return 0;
}
