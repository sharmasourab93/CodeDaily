//New Doubly Linked List 
#include<iostream>
using namespace std;
class DLL{
	public:
		struct Node{
			int data;
			Node *left;
			Node *right;
		};
		Node *newNode(int data){
			Node *temp=new Node();
			temp->data=data;
			temp->left=NULL;
			temp->right=NULL;
			return temp;
		}
		Node *insertNode(Node *head,int data, int pos=0){
			Node *t;t=head;
			cout<<"Insert begin";
			if (head==NULL and pos==0){
				return newNode(data);
			}
			if (pos==0 and t->right!=NULL){
				Node*temp=newNode(data);
				temp->right=head;
				temp->left=head;
				head=temp;
				return head;
			}
			if(pos>1){
				Node *temp=newNode(data);
				while (pos!=0 and t->right->right!=NULL){
					t=t->right;
					pos--;
				}
				Node *t2=t->right;
				t->right=temp;
				temp->right=t2;
				temp->left=t;
				return head;
			}
			cout<<"Insertion Complete"<<endl;
		}
		void deleteNode(Node *head,int data){
			Node *t;t=head;
			while(t->right->data!=data && t->right->right!=NULL){
					t=t->right;
				}
				Node *t1=t->right;
				t->right=t1->right;
				t1->right->left=t;
				delete(t1);
			cout<<"Delete Complete"<<endl;
		}
		void printLL(Node *head){
			Node *temp=head;
			while (temp!=NULL){
				cout<<temp->data<<endl;
				temp=temp->right;
			}
		}
		void operations(){
			Node *head=insertNode(head,21);
			head=insertNode(head,22,1);
			head=insertNode(head,23,1);
			printLL(head);
			deleteNode(head,22);
			printLL(head);
		}
};
int main(){
	DLL dll;
	dll.operations();
}
