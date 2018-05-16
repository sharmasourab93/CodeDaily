#include<stdio.h>
int main(){
	int x=5;
	int* p=&x;
	*p=6;
	int** q=&p;
	int ***r=&q;
	printf("\nAddress of x %d",&x);//2293436
	printf("\nAddress of p %d",&p);//2293432
	printf("\n*p %d\n",*p);//6
	printf("\nAddress of q %d",&q);//2293428 address of q
	printf("\n*q %d\n",*q);// 2293436 address of x
	printf("**q %d\n",**q);//6
	printf("\nAddress of r %d",&r);//2293424
	printf("\n*r  %d\n",*r);//2293432 address of p
	printf("*(*r) %d\n",*(*r));//2293436 address of x
	printf("*(*(*r)) %d\n",*(*(*r)));//6

	***r=10;
	printf("x= %d\n",x);
	**q=*p+2;
	printf("x=%d\n",x);
}

