//Linked List Implementation of a Queue 
#include<iostream>
using namespace std;
class Q{
public:
	struct node{
		int data;
		node* next;
	};
	node *front=new node();
	node *rear =new node();
	front->next=rear->next=NULL;
	//Enqueuing or adding an element in the Queue
	/*int enqueue(){
		cout<<"Enter the element to enter: ";
		int x;
		cin>>x;
		node *temp=new node();
		temp->next=NULL;
		temp->data=x;
		if(q->rear==NULL){
			q->front=q->rear=temp;
		}
		q->rear->next=temp;
		q->rear=temp;
		print();
	}*/
	//Dequeuing or removing an element from the Queue
	int dequeue(){
		
	}
	//Printing the elements in the Queue
	int print(){
		
	}
	//Action Block for the Queue
	int action(){
		cout<<"\n\tQueue Program"<<endl;
		int choice;
		for(int i=0;i<100;i++){
			cout<<"Operations of a Queue:"<<endl;
			cout<<"1.Enqueue\n2.Dequeue\n3.Exit"<<endl<<"Enter choice: ";
			cin>>choice;
			switch(choice){
				case 1: 
					break;
				case 2:
					break;
				case 3:
					exit(0);
					break;
				default:
					exit(0);
					break;
			}
				
		}
	}
};
//Main Function
int main(){
	Q q1;
	q1.action();
}
