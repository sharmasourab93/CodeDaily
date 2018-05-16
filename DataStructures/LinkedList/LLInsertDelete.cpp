/*Working with Linked list part 1*/
#include<iostream>
using namespace std;

class llist1{
	public:
		struct Node{
			int data;		//Value of the node
			Node* link;		//Link or address of the node
		};
		Node* head=NULL;
		//function to insert an element at the beginning
		void insertbegin(){//full tick
			Node* temp=new Node();
			int x;
			cout<<"Enter the element to insert in LL";
			cin>>x;
			//initialized In prior
			temp->data=x;
			//If the linked list is not empty
			if(head!= NULL){
				temp->link=head;
				head=temp;
			}
			//If the linked list is empty
			else{
				temp->link=NULL;
				head=temp;	
			}
		}
		//function to insert an element at ith poistion
		void insertati(){//No tick
		
			Node* temp1=new Node();
			Node* temp2=new Node();
			temp2=head;
			int x,pos;
			cout<<"\n Enter the position:";
			cin>>pos;
			cout<<"\nEnter the element:";
			cin>>x;
			temp1->data=x;
			temp1->link=NULL;
			int i=1;
			for(i=0;i<pos-2;i++){
				temp2=temp2->link;
			}
			temp1->link=temp2->link;
			temp2->link=temp1;
			while(temp2!=NULL){
				temp1=temp1->link;
			}
			head=temp1;
		}
		void insertatend(){//No tick
		/*deletes all elements towards the front 
		before execution
		25
		24
		23
		22
		21
		After inserting 30 
		21
		30
		//So this is my doubt here 
		This  is the problem here
		 */
			//function to insert an element at the end of a data structure
			Node* temp=new Node();
			Node* newnode=new Node();
			int x;
			cout<<"\n Enter the element:";
			cin>>x;
			newnode->data=x;
			newnode->link=NULL;
			temp=head;
			while(temp->link!=NULL){
				temp=temp->link;
			}
			temp->link=newnode;
			head=temp;//If this is removed creates error
			//and after changes are made u would definately need to make changes with head pointer right then how will it be altered??
			
		}
		void deleteatbegin(){//perfect tick
			//function to delete an element at the beginning
			Node* delold=new Node();
			delold=head;
			int i;
			head=delold->link;
			delete delold;
		}
		void deleteati(){
			//function to delete an element at the ith position
			Node* deli=new Node();
			deli=head;
			int pos;
			cout<<"\nEnter the position";
			cin>>pos;
			for(int i=0;i<pos-1;i++){
				deli=deli->link;
				
			}
			head->link=deli->link;
			delete deli;
		}
		void deleteatend(){//partial tick
			//function to delete an element at the end
			Node*dele1=new Node();
			Node* temp=new Node();
			dele1=head;
			while(dele1->link!=NULL){
				if(dele1->link->link==NULL){
					temp=dele1->link;
					dele1->link=temp->link;
					delete(temp);
				}
				dele1=dele1->link;
				cout<<dele1->data<<endl;
			}
			head=dele1;
		}
		void printlist(){
			Node* temp=new Node();
			temp=head;
			while(temp!=NULL){
				cout<<"Element"<<(temp->data)<<endl;
				temp=temp->link;
				
			}
		}
		void reverse(){
			//if(head == NULL) return;
    		Node* prev = NULL;
			Node* current = NULL; 
			Node* next = NULL;
    		current = head;
    		while(current != NULL){
        		next = current->link;
        		current->link= prev;
        		prev = current;
        		current = next;
    		}
    		// now let the head point at the last node (prev)
    		head = prev;
		}
		void choiceopt(){//Tick
			int x=0;
			for(int i=0;i<100;i++){
				if(i==0){
					//takes you to insert at beginning function at the first instance of the loop
					insertbegin();
				}
				while(i!=0){
					cout<<"\n Welcome to the class linked list";
					cout<<"\n Options to Choose:";
					cout<<"\n1.Insert an Element at beginning";
					cout<<"\n2.Insert an Element at the ith position";
					cout<<"\n3.Insert an Element at the end";
					cout<<"\n4.Delete an element at the front";
					cout<<"\n5.Delete an element at the ith position";
					cout<<"\n6.Delete an element at the end";
					cout<<"\n7.Print the Linked list";
					cout<<"\n8.Reverse the Linked List";
					cout<<"\n9.Exit";
					int choice;
					cout<<"\nEnter your choice:";
					cin>>choice;
					switch (choice){
						case 1:
						insertbegin();
						break;
						case 2: 
						insertati();
						break;
						case 3: 
						insertatend();
						break;
						case 4: 
						deleteatbegin();
						break;
						case 5: 
						deleteati();
						break;
						case 6: 
						deleteatend();
						break;
						case 7:
						printlist();
						break;
						case 8:
						reverse();
						case 9:
						exit('\0');
				}		
			}
		}
	}
		
};
int main(){
	llist1 x;
	x.choiceopt();
}

