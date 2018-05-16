#include<stdio.h>
int main()
{
	int x=5;
	int *p;
	p=&x;
	int **q=(&p);
	int ***z=&q;
	printf("\nAddress x %d",&x);
	//printf("\nAddress x %d",p); address of x 32
	printf("\nAddress p %d",&p);//address of p 28
	printf("\n*p %d",*p);//5
	printf("\nAddress q %d",&q);//address of q 24
	printf("\nq %d ",q);//28
	printf("\n*q %d ",*q);//32
	printf("\n**q %d",**q);//5
	printf("\n***z %d",***z);
	printf("\n**z %d",**z);
	printf("\n*z %d",*z);
	printf("\nz %d",z);
	printf("\n&z %d",&z);

	printf("\n Size of *p, **q,***z %d  %d  %d",sizeof(*p),sizeof(**q),sizeof(***z));
}
