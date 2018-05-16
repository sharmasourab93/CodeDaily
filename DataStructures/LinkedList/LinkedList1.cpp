//Datastructures Linked List Implementation of a Stack
#include<iostream>
using namespace std;
class LinkedList1{	
public:
	struct node{
		int data;
		node *next;
	};
	node *head=NULL;
	int push(int x){
		node *temp=new node();
		temp->data=x;
		temp->next=NULL;
		//If Linked List is not equal to null
		if(head!=NULL){
			temp->next=head;
			head=temp;
		}
		//If Linked List equal to Null
		else{
			temp->next=head;
			head=temp;
		}
		print();	
	}	
	int pop(){
		string s="No Elements Found!";
		node *temp=new node();
		peek();
		temp=head;
		head=temp->next;
		return head->data;
		//delete(temp);
	}
	int print(){
		node *temp1=new node();
		temp1=head;
		while(temp1!=NULL){
			cout<<temp1->data<<endl;
			temp1=temp1->next;
		}
	}
	int peek(){
		cout<<head->data<<endl;
	}
	int reverse(){
		cout<<"Reversing..."<<endl;
		node* prev=new node();
		node* next=new node();
		node* current=new node();
		current=head;
		while(current!=NULL){
			next=current->next;
			current->next=prev;
			prev=current;
			current=next;
		}
		head=prev;
		print();
	}
	int action(){
		cout<<"Linked List Program for stack"<<endl;
		for(int i=0;i<100;i++){
			cout<<"1.Push\n2.Pop\n3.Peek\n4.Reverse"<<endl;
			cout<<"Enter Choice:";
			int choice;
			cin>>choice;
			switch(choice){
				case 1:
					cout<<"Enter the element to push:";
					int p;
					cin>>p;
					push(p);
					break;
				case 2:
					cout<<"Poping..."<<pop()<<endl;
					break;
				case 3:
					cout<<"Peeking.."<<endl;
					peek();
					break;
				case 4:
					reverse();
					break;
				default:
					exit(0);
					break;
				}
		}
	}
};
int main()
{
	LinkedList1 ll;
	ll.action();
}
