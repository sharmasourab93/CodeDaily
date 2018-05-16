//Making a simple Linked List program to insert a function
#include<iostream>
using namespace std;
struct Node{
	int data;
	Node* next;
};
Node* head=NULL;
void insertati(int x){
	int value, pos, counter = 0; 
    Node *temp, *s, *ptr;
    temp->data=x;
    cout<<"Enter the postion at which node to be inserted: ";
    cin>>pos;
    int i;
    s=head;
    while (s!=NULL)
    {
        s=s->next;
        counter++;
    }
    if (pos!=1)
    {
        /*if (start == NULL)
        {
            start = temp;
            start->next = NULL;
        }
        else*/
        
            ptr = head;
            head= temp;
            head->next = ptr;
        
    }
    else if (pos > 1  && pos <= counter)
    {
        s = head;
        for (i = 1; i < pos; i++)
        {
            ptr = s;
            s = s->next;
        }
        ptr->next = temp;
        temp->next = s;
    }
    else
    {
        cout<<"Positon out of range"<<endl;
    }
	
}
void insert(int x){
	//Function to insert a data into the linked list
	//Only to insert numbers at the beginnging
	Node* temp=new Node();
	temp->data=x;
		//If Linked list is already filled
		if(head!=NULL){
			//temp->data=x;
			temp->next=head;
			head=temp;
		}
		else{
			//temp->data=x;
			temp->next=NULL;
			head=temp;
		}
}
void print(){
	Node* temp=new Node();
	temp=head;
	while(temp!=NULL){
		cout<<temp->data<<endl;
		temp=temp->next;
	}
}
void option(int i){
		int x;
		cout<<"\nEnter the option\n\t1.At front\n\t2.At the specified positon";
		cin>>x;
		if(x==1){
			int a;
			cout<<"\nEnter the number";
			cin>>a;
			insert(a);
			print();
		}else{
			int b;
			cout<<"\nEnter number:";
			cin>>b;
			insertati(b);
			print();
			
		}
}
int main(){
	cout<<"\nWhat size of datastructures?";
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
		
		option(i);
	}
}
