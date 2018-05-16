#include<stdio.h>
int main(){
	int i=4,j=30,k;
	k=j++/i++;
	++k;
	printf("%d,%d,%d",i,j,k);
}
