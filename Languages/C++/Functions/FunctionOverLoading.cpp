/*operator overloading*/
#include<iostream>
using namespace std;
class oploading{
	public:
	void add(int a,int b){
		int c;
		c=a+b;
		cout<<c;
	}
	void add(float a, float b){
		float c;
		c=a-b;
		cout<<c;
	}
	
};
int main(){
	oploading x;
	int a,b,c;
	float a1,b1,c1;
	cout<<"\nIntegers:";
	cin>>a;
	cin>>b;
	x.add(a,b);
	cout<<"\nFloating Point Constansts";
	cin>>a1;
	cin>>b1;
	x.add(a1,b1);
	
}
