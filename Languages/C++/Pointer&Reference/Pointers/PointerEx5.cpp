#include<stdio.h>
int main(){
	int a=5;
	int *p;//pointer to int
	int b=20;
	char c;
	char *po;//pointer to character
	double d;
	double *p1;//pointer to double
	
	p=&a;//accessing base address
	 printf("\nPrinting the address of a %d",p);
	 //value of a=5 so is *p=5
	 printf("\nPrinting the value of *p %d",*p);
	 printf("\nPrinting the value of *p+1 %d",*(p+1));//20
	 *p=b;//changing the value of a via *p
	 //value of p remains the same
	printf("\nPrinting the address of &a %d",p);//address of a
	 //value of *p after changing
	 printf("\nPrinting the value of *p %d",*p);//20
	 printf("\nPrinting the value of a %d",a);//20
	 // value of a changes when *p is assigned to b;
	printf("\nChanging the address value %d",p+1);//address+1(4)
	//value of the address takes to the next address after int
	printf("\nChanging the value of *p %d",*p+1);//*21
}
