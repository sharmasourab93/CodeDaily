//Calling static function in  a class
#include<iostream>
using namespace std;

class St{
	public:
		static int i;
		static void func(){
			cout<<"I'm static function bhidu";
		}
		void printval(){
			cout<<i<<endl;
		}
};
int St::i=10;
int main(){
	St s;
	s.func();
	cout<<s.i;
}
