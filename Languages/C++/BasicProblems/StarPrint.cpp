/*Drawing a Number triangle
*/
#include<iostream>
using namespace std;
int main(){
	int a;
	cout<<"\nEnter a number:";
	cin>>a;
	int i,b=a;
	while(a>=1){
		for(i=a;i>=1;i--){
			cout<<"*";
		}
		a--;
		cout<<endl;
	}
	while(i!=b+1){
		for(i=1;i<a;i++){
			cout<<"*";
		}
		a++;
		cout<<endl;
	}
	
	
}
