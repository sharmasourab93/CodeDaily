//String split
#include<iostream>
#include<string.h>
using namespace std;
int main(){
	char str[]="Geeks-for-Geeks";
	
	char *token=strtok(str,"-");
	cout<<token[5]<<endl;
	while(token!=NULL){
		cout<<token<<endl;
		token=strtok(NULL,"-");
	}
}
