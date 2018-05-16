#include<iostream>
int main(){
	//Working with pointers as a revision
	int *p;
	int b=10;
	p=&b;
	printf("\nPrinting the number %d",*p);
	int a=15;
	p=&a;
	printf("\nPrinting the revised number %d",*p);
	int **q;
	q=&p;
	printf("\n%d the Number q is ",q);
	printf("\n%d the Number q is ",*q);
	printf("\n%d the Number q is ",**q);
	
}
