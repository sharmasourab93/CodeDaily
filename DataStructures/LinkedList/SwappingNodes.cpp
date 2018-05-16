#include<iostream>
using namespace std;
class SwapNodes{
	public:
		struct Node{
			int data;
			Node *next;
		};
		void push(Node *root, int data){
			Node *temp;
			temp->data=data;
			temp->next=root;
			root=temp;
		}
		Node *findNode(Node* root, int data){
			Node *temp,*temp1;
			temp=root;
			while(temp!=NULL){
				if(temp->next->data==data){
					temp1=temp->next;
					//temp1->next
					return temp1;
				}
				temp=temp->next;
			}
		}
		void printNodes(Node *root){
			while(root!=NULL){
				cout<<root->data<<" ";
				root=root->next;
			}
			cout<<endl;
		}
		void swapNodes(Node *root,Node *pre, Node *suc){
			Node *t,*temp,*temp1;
			t=root;
			temp=pre->next;
			temp1=suc->next;
			while(t!=NULL){
				if(t->next->data==pre->data){
					t->next=suc;
					t->next->next=temp;
				}
				t=t->next;
			}
			while(t!=NULL){
				if(t->next->data==suc->data){
					t->next=pre;
					t->next->next=temp1;
				}
				t=t->next;
			}
		}
		void driver(){
			Node *root=new Node();
			push(root,5);
			push(root,4);
			push(root,3);
			push(root,2);
			push(root,1);
			Node *pre,*suc;
			printNodes(root);
			pre=findNode(root,2);
			suc=findNode(root,4);
			swapNodes(root,pre,suc);
			printNodes(root);
			
		}
};
int main(){
	SwapNodes sn;
	sn.driver();
}
