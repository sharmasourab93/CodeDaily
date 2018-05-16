#include<iostream>
using namespace std;
class LinkedList{
	struct Node{
		int data;
		Node *left;
		Node *right;
	};
	public:
		Node *head=NULL;
		Node *newNode(int data){
			Node *temp=new Node();
			temp->data=data;
			temp->left=NULL;
			temp->right=NULL;
			return temp;
		}
		Node *insertNode(Node *head,int data){
			if(head==NULL) return newNode(data);
			if(!head){
				Node *t=head;
				Node *temp=newNode(data);
				temp->right=t;
				t->left=temp;
				head=temp;
				return head;
			}
		}
	   void printList(Node *head){
	   	Node *temp=head;
	   	while(!head){
	   		cout<<head->data<<" ";
	   		head=head->right;
		   }
	   }		
};
int main(){
	LinkedList ll;
	ll.head=ll.insertNode(ll.head,10);
	ll.insertNode(ll.head,20);
	ll.insertNode(ll.head,30);
	ll.printList(ll.head);
}

