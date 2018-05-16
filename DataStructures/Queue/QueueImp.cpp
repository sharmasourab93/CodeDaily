//Implementation of Queue Data Structure 
#include<iostream>
using namespace std;
class Q{
	public:
		//Structure of QNode
		struct QNode{
			int data;
			QNode * next;
		};
		//Structure of Queue
		struct Queue{
			QNode* front=NULL, *rear=NULL;
		};
		//Utility function at enqueue
		void enqueue(Queue *q,int data){
			QNode * temp;
			temp->data=data;
			temp->next=NULL;
			if(q->rear==NULL){
				q->front=q->rear=temp;
				return;
			}
			q->rear->next=temp;
			q->rear=temp;	
		}
		//Utility function to Dequeue elements from stack
		int dequeue(Queue *q){
			if(q->front==NULL){
				return NULL;
			}
			QNode* temp=q->front;
			q->front=q->front->next;
			if(q->front==NULL){
				q->rear=NULL;
				return temp;
			}
		}
};
int main(){
	
}
