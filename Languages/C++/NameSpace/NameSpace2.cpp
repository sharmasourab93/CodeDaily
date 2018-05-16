#include<iostream>
using namespace std;
namespace firstclass{
	class funckme{
		public:
			int x;
			funckme(){
				cout<<"ahhh !";
			}
			void job(){
				cout<<"\nEnter X";
				cin>>x;
				cout<<"X is:"<<x<<endl;
			}
			
	};
}
//using namespace firstclass;
int main(){
	firstclass::funckme x;
	x.job();
	
}
