#include<stdio.h>
int main(){
	FILE *fp;
	fp=fopen("sourab.txt","w+");
	fprintf(fp,"Beta1 This is Ninja1 testing");
	fputs("Ninja1 this Beta1 responding",fp);
	fclose(fp);
}
