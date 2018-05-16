#include<iostream>
using namespace std;
class LListCount{
	public:
		struct Node{
			int data;
			int count;
			Node* next;
		};
		Node* newNode(Node* temp,int data);
		int traverse(Node* temp,int data);
		void incrementCount(Node* temp,int data);
		void push(Node* temp,int data);
		void printlist(Node* temp);
		void driver();
};
int main(){
	LListCount ll;
	ll.driver();
}
void LListCount::traverse(Node* temp,int data){
	
}
