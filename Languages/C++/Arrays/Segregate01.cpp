//Segregate 0s and 1s in an array
#include<iostream>
#include<vector>
#include<iterator>
using namespace std;
struct Node{
	int data;
	int count;
	Node* next;
};
Node *head=NULL;
Node* newNode(int data){
	Node *node=new Node();
	node->data=data;
	node->count++;
	node->next=NULL;
	return node;
}
int traverse(int data){
	Node * temp=NULL;
	temp=head;
	while(temp->next!=NULL){
		if(temp->data==data){
			return data;
		}else{
			temp=temp->next;
		}
	}
}
void incrementCount(int data){
	Node* temp=NULL;
	temp=head;
	while(temp->next!=NULL){
		if(temp->data==data){
			temp->count++;
		}else{
			temp=temp->next;
		}
	}
}
void push(int data){
	Node* temp=NULL;
	temp->data=data;
	temp->count++;
	temp->next=head;
	head=temp;
}
void printLList(){
	Node *temp=NULL;
	temp=head;
	while(temp->next!=NULL){
		cout<<" Data: "<<temp->data<<" "<<"Count: "<<temp->count<<endl;
		temp=temp->next;
	}
}
int main(){
	int array[]={0,0,1,1,1,0,1,0,1,1,0,0,0,0,1,1,1};
	int size=sizeof(array)/sizeof(array[0]);
	int j=0;
	head=newNode(array[0]);
	for(int i=0;i<size;i++){
		if(array[i]==traverse(head->data)){
			incrementCount(array[i]);
		}else{
			push(array[i]);
		}
	}
	printLList();
}
