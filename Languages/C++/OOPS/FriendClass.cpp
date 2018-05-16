//FriendClass
#include<iostream>
using namespace std;
class Node{
	private:
		int data;
		Node *next;
		friend class LinkedList::search();
};

class LinkedList{
	public:
		Node *head=NULL;
		void search(){
			Node * node=new Node();
			node->data=10;
			node->next=NULL;
			cout<<node->data<<endl;
		}
};
int main(){
	LinkedList ll;
}
