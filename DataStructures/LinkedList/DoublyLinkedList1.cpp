//Implementation of a doubly Linked List
#include<iostream>
using namespace std;
class dlinkedlist{
public:
	struct node{
		int data;
		node *prev;
		node *next;
	};
	node *head=NULL;
//Function to Insert an element into the linked list
	int insert(){
		node *temp=new node();
		node *temp1=new node();
		temp1=head;
		int pos,info;
		cout<<"Enter data: ";
		cin>>info;
		temp->data=info;
		cout<<"\nEnter position:\n1.Begin\n2.End\n3.At a given position ";
		cin>>pos;
		switch(pos){
			case 1://Inserting at the beginning of the list
			//Inserting at the begin when head=NULL
				if(head==NULL){
					temp->next=head;
					temp->prev=NULL;
					head=temp;
				}
				//Inserting at the begin when head!=NULL
				else{
					temp->next=head;
					head=temp;
				}
				break;
			case 2:
			//Inserting at the end of the list
				while(temp1->next!=NULL){
					temp1=temp1->next;
				}
				temp->prev=temp1;
				temp1->next=temp;
				temp->next=NULL;
				break;
			case 3:
			//Inserting at any given position
				cout<<"Enter the position: ";
				int posi;
				cin>>posi;
				for(int i=0;i<posi-1;i++){
					temp1=temp1->next;	
				}
				temp->next=temp1->next;
				temp1->next=temp;
				temp->prev=temp1;
				break;
				}
		print();
		cout<<endl;
			}
//Function to Delete an element from the lInked list at various positions
	int deletelist(){
		cout<<"Enter position to delete.\n1.Begin\n2.End\n3.At a given position: ";
		node *temp=new node();
		node *temp1=new node();
		temp=head;
		int opt;
		cin>>opt;
		switch(opt){
			case 1:
				//Deleting an element at the begin
				temp=temp->next;
				temp->prev=NULL;
				head=temp;
				break;
			case 2:
				//Deleting an element towards the end
				while(temp->next->next!=NULL){
					temp=temp->next;
				}
				temp->next=NULL;
				break;
			case 3:
				//Deleting linked list At a given position
				cout<<"Enter Position: ";
				int p;
				cin>>p;
				for(int i=0;i<p-1;i++){
					temp=temp->next;
				}
				temp->next=temp->next->next;
				temp->next->prev=temp;
				break;
			}
		print();
		cout<<endl;
	}
	//Printing the linked list
	int print(){
		node * temp=new node();
		temp=head;
		int count=0;
		while(temp!=NULL){
			cout<<temp->data<<" ";
			temp=temp->next;
			count++;
		}
		//Keeping a count of the elements
		cout<<"\nSize[No. of Elements] of the linked list "<<count<<endl;
	}
//Function to reverse the doubly Linked List
	int reverse(){
		node *temp=new node();
		node *current=new node();
		current=head;
		while(current!=NULL){
			temp=current->prev;
			current->prev=current->next;
			current->next=temp;//Swapping upto this point
			current=current->prev;	//traversing to the next element in head
		}
		head=temp->prev;
		print();
	}
	int action(){
		cout<<"Doubly Linked List Program...."<<endl;
		for(int i=0;i<100;i++){
			cout<<"Enter your choice:"<<endl;
			cout<<"1.Insert\n2.Delete\n3.Reverse\n4.Exit ";
			int choice;
			cin>>choice;
			switch(choice){
				case 1:
					insert();
					break;
				case 2:
					deletelist();
					break;
				case 3:
					reverse();
					break;
				default:
					exit(0);
			}
		}
	}
};
int main(){
	dlinkedlist dll;
	dll.action();
}
