#include<stdio.h>
int main()
{
	int a=1025;
	int *p=&a;
	printf("Size of the integer is %d bytes",sizeof(int));//4
	printf("\nAddress %d  Value=%d",p,*p);//address, 1025
	char* p0;
	p0=(char*)p;//type casting
	printf("\nSize of char is %d bytes\n",sizeof(char));
	//1025=0000000000000000 0000010000000001
	//dereferencing to char will look just one byte of data.
	printf("Address=%d, value=%d\n",p0,*p0);
	//returns 1 bcoz will read the 1st byte of the data after typecasting.
	printf("Address=%d, value=%d\n",p0+1,*(p0+1));
	// returns 4 bcozwill read the second byte of the data

	}
	

