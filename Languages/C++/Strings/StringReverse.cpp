//Reverse String 

#include<bits/stdc++.h>
using namespace std;
void swap(char *str1,char *str2){
	char *temp;
	temp=str1;
	str1=str2;
	str2=temp;
}

/*string reverse(string str){
	int n=str.length();
	for(int i=0;i<n/2;i++){
		swap(str[i],str[n-1-i]);
	}
	return str;
}*/
int main(){
	string str="geeksforgeeks";
	//str=reverse(str);
	reverse(str.begin(),str.begin()+5);
	cout<<str<<endl;
	cout<<str.find("g",0);
}
