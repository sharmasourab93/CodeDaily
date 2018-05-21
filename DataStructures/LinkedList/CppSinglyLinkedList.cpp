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

		//To Print elements in reverse order
		void printreverse(Node *root){
			if(root==NULL) return ;
			Node *temp=new Node();
			temp=root;
			printreverse(temp->next);
			std::cout<<temp->data<<" ";
			
		}
		
		//The Recursive method to Reverse the Nodes in the linkedlist 
		void reverse(Node *curr,Node *prev,Node **head){
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

		//Iterative method of Reversing the nodes in the linked List
		void Ireverse(){
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
		}

		//Swap Two Nodes
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

		//Swapping Linked List by looking for two different elements
		void swap(int x,int y ){
			if(x==y) return ;
			//search for x(keep track of prevX and CurrX)
			Node *prevX=NULL,*currX;
			currX=head;
			while(currX && currX->data!=x){
				prevX=currX;
				currX=currX->next;
			}
			//Search for y(keep track of prevY and CurrY
			Node *prevY=NULL,*currY;
			currY=head;
			while(currY && currY->data!=y){
				prevY=currY;
				currY=currY->next;
			}
			//If either x or y is not present, nothing to do 
			if(currX==NULL||currY==NULL) return;
			if(prevX!=NULL) prevX->next=currY;
			else *head=*currX;
			if(prevY!=NULL) prevY->next=currX;
			else *head=*currX;
			
			Node* temp=currY->next;
			currY->next=currX->next;
			currX->next=temp;
		}

		void printLL(Node *root){
			while(root!=NULL){
				std::cout<<root->data<<" ";
				root=root->next;
			}
			std::cout<<std::endl;
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
			printreverse(root);
			cout<<"\nReversing the node: "<<endl;
			reverse(root,NULL,&root);
			printLL(root);
		}
};
int main(){
	LinkedList ll;
	ll.driver();
}
