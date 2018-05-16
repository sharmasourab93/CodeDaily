//Rotational Linked List
/*
*Given a singly linked list, rotate the linked list counter-clockwise by k nodes.
*Where k is a given positive integer. 
*For example, if the given linked list is 10->20->30->40->50->60 and k is 4, the list should be modified to 50->60->10->20->30->40. 
*Assume that k is smaller than the count of nodes in linked list.
*/
#include<iostream>
using namespace std;
class Rll{
	public:
		struct node{
			int data;
			node* next;
		};
		node* Head=NULL;
		void insert(int ele){
			node *temp=NULL;
			temp->data=ele;
			temp->next=NULL;
			if(Head){
				
			}
		}
		void rotate(int k){
			node *temp=NULL;
			temp=Head;
			int i=1;
			while(i<k+1){
				temp=temp->next;
				i++;
			}
			node* temp1=NULL;
			temp1=temp;
			while(temp1!=NULL){
				temp1=temp1->next;
			}
			temp1->next=temp;
			Head=temp1;
			print();
		}
		void print(){
			node *temp=NULL;
			temp=Head;
			cout<<endl;
			while(temp!=NULL){
				cout<<temp->data<<"\t";
				temp=temp->next;
			}
		}
		int choice(){
			int arr[]={10,20,30,40,50,60,70};
			for(int j=0;j<sizeof(arr);j++){
				insert(arr[j]);
			}
			print();
			cout<<"Rotation Element: ";
			int rot;
			cin>>rot;
			rotate(rot);
		}
};
int main(){
	Rll r;
	r.choice();	
}
