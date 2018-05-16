#include<iostream>
using namespace std;
class String{
		int len;
		char *str;
	public:
		String operator =(const String &1){
			S1.len=this->len;
			S1.str=this->str;

		}

		String(const String &S1){
			this->len=S1.len;
			this->str=S1.str;
		}
}


void Anagram(char *str1,char *str2, int n1,int n2){
	
	if(n1!=n2){
		cout<<"The given strings are not an anagram"<<endl;
		return;
	}
	int i=0;
	int num[26]={0};
	while(str1[i]!=NULL){
		num[str2[i]-'a']++;
		i++;
	}

}

char *reverstring(char *str, int n1){
	char temp[n1];
	int j=0;
	for(int i=n1-1;i>=0;i--){
		temp[j]=str[i];
		j++;
	}

	return temp;
}