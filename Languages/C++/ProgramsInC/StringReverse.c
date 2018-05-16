//String reverse without using Strrev
#include<stdio.h>
#include<string.h>
void reverse(char a[30]){
	char temp;
	int b=0,c=(strlen(a)-1),d;
	while(b<c){
		temp=a[b];
		a[b]=a[c];
		a[c]=temp;
		b++;
		c--;
	}
	printf("\n%s",a);
}
int main(){
	int i=0,j=0,count=0;
	char x[30]="Sourab Sharma";
	//printf("%s",strrev(x));
	reverse(x);
}
