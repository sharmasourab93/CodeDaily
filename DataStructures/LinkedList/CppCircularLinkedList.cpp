//Circular LinkedList
//Source: GeeksforGeeks
#include<iostream>
#include<stdlib.h>
using namespace std;
struct Node{
	int data;
	Node *next;
};
struct Node *addToEmpty(Node *last,int data){
	//This function is only for empty list
	if(last!=NULL) return last;
	//creating a node dynamically
	Node *temp=new Node();
	//Assigning the data
	temp->data=data;
	last=temp;
	//Creating the circular link;
	last->next=last;
	return last;
}
struct Node *addBegin(Node *last,int data){
	if(last==NULL) return addToEmpty(last,data);
	Node *temp=new Node();
	temp->data=data;
	temp->next=last->next;
	last->next=temp;
	
	return last;
}
struct Node *addEnd(Node *last,int data){
	if(last==NULL) return addToEmpty(last,data);
	Node *temp=new Node();
	temp->data=data;
	temp->next=last->next;
	last->next=temp;
	last=temp;
	return last;
}

struct Node *addAfter(Node *last,int data,int item){
	if(last==NULL) return NULL;
	Node *temp,*p;
	p=last->next;
	do{
		if(p->data==item){
			temp=new Node();
			temp->data=data;
			temp->next=p->next;
			p->next=temp;
			
			if(p==last){
			 last=temp;
			 return last;
			}
		}
		p=p->next;
	}while(p!=last->next);
	return last;
}
void traverse(Node *last){
	Node *p;
	if(last==NULL){
		cout<<"list is empty"<<endl;
		return;
	}
	p=last->next;
	do{
		cout<<p->data<<" ";
		p=p->next;
	}while(p!=last->next);
}
int main(){
	Node *last=NULL;
	last=addToEmpty(last,6);
	last=addBegin(last,4);
	last=addBegin(last,2);
	last=addEnd(last,8);
	last=addEnd(last,12);
	last=addAfter(last,10,8);
	traverse(last);
}
