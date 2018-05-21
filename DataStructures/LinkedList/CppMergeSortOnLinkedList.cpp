#include<iostream>
using namespace std;

class linkedlist{
	public:
		struct Node{
			int data;
			Node *next;
			Node *prev;
		};
		Node *split(Node *head){
			Node *slow=head,*fast=head;
			while(fast->next && fast->next->next){
				fast=fast->next->next;
				slow=slow->next;
			}
			Node *temp=slow->next;
			slow->next=NULL;
			return temp;
		}
		Node* merge(Node *first,Node *second){
			cout<<"\nMerge Method"<<endl;
			if(!first) return second;
			if(!second) return first;
			if(first->data<second->data){
				first->next=merge(first->next,second);
				first->next->prev=first;
				first->prev=NULL;
				return first;
			}
			else{
				second->next=merge(first,second->next);
				second->next->prev=first;
				second->prev=NULL;
				return second;
			}
		}
		Node* mergesort(Node *head){
			cout<<"\nMergeSort"<<endl;
			if(head==NULL || head->next==NULL) return head;
			Node *second=split(head);
			head=mergesort(head);
			second=mergesort(second);
			return merge(head,second);
		}
		Node* insert(Node *head,int data){
			Node *temp=new Node();
			temp->data=data;
			temp->next=temp->prev=NULL;
			if (!head){
				head=temp;
				return head;
			}else{
				temp->next=head;
				head->prev=temp;
				head=temp;
				return head;
			}
		}
		void print(Node *head){
			Node *temp=head;
			while(temp!=NULL){
				cout<<head->data<<" ";
				temp=head;
				head=head->next;
			}
		}
		void operations(){
			Node *head=NULL;
			head=insert(head,5);
			head=insert(head,10);
			head=insert(head,25);
			head=insert(head,35);
			head=insert(head,45);
			print(head);
			head=mergesort(head);
			cout<<"\nLinked List after sorting"<<" ";
			print(head);
		}
};
int main(){
	linkedlist ll;
	ll.operations();
}
