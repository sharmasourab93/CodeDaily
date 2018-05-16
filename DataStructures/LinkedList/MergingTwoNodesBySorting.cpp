//Singly Linked List
//Revision
#include<iostream>
#define MAX 10
using namespace std;
class Sll{
	public:
		struct Node{
			int data;
			Node* next;
		};
		struct Node *newNode(int data){
			Node * newnode=new Node();
			newnode->data=data;
			newnode->next=NULL;
			return newnode;
		}
		Node *head=NULL;
		int addNode(int position, int data){
			int pos=0;
			if(position==0){
				Node * nnode=newNode(data);
				nnode->next=head;
				head=nnode;
			}else if(position>0){
				Node * temp=newNode(data);
				Node * temp1=new Node();
				Node *temp2=new Node();
				temp1=head;
				while(temp1->next!=NULL && pos<position){
					temp1=temp1->next;
					pos++;
				}
				temp2=temp1->next;
				temp->next=temp2;
				temp1->next=temp;
			}
		}
		int deleteNode(int position){
			int pos=0;
			if(position==0){
				Node *nnode=new Node();
				nnode=head->next;
				head=nnode;
			}else if(position>0){
				Node *temp=new Node();
				Node *temp1=new Node();
				Node *temp2=new Node();
				temp1=head;
				while(temp1->next!=NULL && pos<position){
					temp1=temp1->next;
					pos++;
				}
				temp2=temp1->next;
				temp1->next=temp1->next->next;
				delete(temp2);
			}
		}
		void reverse(){
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
		void printNode(){
			Node * temp=new Node();
			temp=head;
			while(temp!=NULL){
				cout<<temp->data<<" ->";
				temp=temp->next;
			}
		}
		void recurse(){
			int option;
			int position;
			int data;
			while(!false){
				cout<<"\nSingly Linked List Operation";
				cout<<"\n1.Add\n2.Delete\n3.Print\n4.Reverse ";
				cin>>option;
				switch(option){
					case 1:
						cout<<"\nEnter add position and data ";
						cin>>position;
						cin>>data;
						addNode(position,data);
						break;
					case 2:
						cout<<"\nEnter position of delete ";
						cin>>position;
						deleteNode(position);
						break;
					case 3:
						cout<<"\n Printing Nodes..."<<endl;
						printNode();
						break;
					case 4:
						cout<<" Reversing..."<<endl;
						reverse();
						break;
					default:
						exit(0);
				}	
			}	
		}
};
int main(){
	Sll sll;
	sll.recurse();
}
