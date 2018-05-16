//Reversing a linked List 
#include<iostream>
using namespace std;
class LinkedList{
	public:
		struct Node{
			int data;
			Node *next;
		};
		Node *newNode(int data){
			Node *newnode=new Node();
			newnode->data=data;
			newnode->next=NULL;
			return newnode;
		}
		Node *push(Node *root,int data){
			Node *temp=newNode(data);
			temp->next=root;
			root=temp;
			return root;
		}
		void printLL(Node *root){
			while(root!=NULL){
				std::cout<<root->data<<" ";
				root=root->next;
			}
			std::cout<<std::endl;
		}
		//To Print elements in reverse order
		void reverse(Node *root){
			if(root==NULL) return ;
			Node *temp=new Node();
			temp=root;
			reverse(temp->next);
			std::cout<<temp->data<<" ";
			
		}
		//Iterative method of Reversing the nodes in the linked List
		/*void reverse(){
			Node * current=new Node();
			Node *next=new Node();
			Node *prev=new Node();
			prev=NULL;
			current=head;
			while(current!=NULL){
				next=current->next;
				current->next=prev;
				prev=current;
				current=next;
			}
			head=prev;
		}*/
		//The Recursive method to Reverse the Nodes in the linkedlist 
		void reverse(Node *curr,Node * prev,Node **head){
			//**in Head is essential here
			if(!curr->next){
				*head=curr;
				curr->next=prev;
				return;
			}
			Node *next=curr->next;
			curr->next=prev;
			reverse(next,curr,head); 
		}
		void driver(){
			Node *root=newNode(1);
			root=push(root,2);
			root=push(root,3);
			root=push(root,4);
			root=push(root,5);
			root=push(root,6);
			printLL(root);
			cout<<"\nPrinting the LinkedList in reverse order:"<<endl;
			reverse(root);
			cout<<"\nReversing the node: "<<endl;
			reverse(root,NULL,&root);
			printLL(root);
		}
};
int main(){
	LinkedList ll;
	ll.driver();
}
