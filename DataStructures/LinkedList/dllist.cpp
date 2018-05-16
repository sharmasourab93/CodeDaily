//Doubly Linked List 
#include<iostream>
using namespace std;
class dllist{
	public:
		struct Node{
			int data;
			Node* Rnode;
			Node* Lnode;
		};
		Node *head=NULL;
		//to insert element into the linked list
		
		//Insert From the Beginning 
		void begin(){
			Node* temp=new Node();
			cout<<"\nEnter data";
			int x;
			cin>>x;
			temp->data=x;
			if(head==NULL){
				temp->Rnode=NULL;
				head=temp;
			}else if(head!=NULL){
				temp->Rnode=head;
				head=temp;
			}
			print();
		}
		//Insert at the given position
		void insertI(int* p){
			int i=0,x;
			Node* temp=new Node();
			temp=head;
			cout<<"\nEnter data: ";
			cin>>x;
			Node* newtemp=new Node();
			newtemp->data=x;
			while(temp!=NULL && i<*p){
				temp=temp->Rnode;
				i++;
			}
			newtemp->Rnode=temp->Rnode;
			temp->Rnode=newtemp;
			newtemp->Lnode=temp;
			head=temp;
		}
		//Insert from the end
		void insertend(){
			Node* newNode=new Node();
			Node* last=head;
			int x;
			
			cout<<"\nEnter data: ";
			cin>>x;
			newNode->data=x;
			while(last->Rnode==NULL){
				last=last->Rnode;
			}
			last->Rnode=newNode;
			newNode->Lnode=last;
			print();
			
		}
		void insertelement(){
			cout<<"Where do you wish to enter the elements?"<<endl;
			cout<<"\t1.Begining"<<endl;
			cout<<"\t2.Given postiion"<<endl;
			cout<<"\t3.End"<<endl;
			int choice;
			cin>>choice;
			switch(choice){
				case 1:
					begin();
					break;
				case 2:
					int pos;
					cout<<"\nEnter position"<<endl;
					cin>>pos;
					insertI(&pos);
					break;
				case 3:
					insertend();
					break;
			} 
		}
		//to delete element from the linked list
		void delbegin(){
			Node* newNode=new Node();
			Node* temp=head;
			newNode->Rnode=temp->Rnode;
			newNode->Lnode=NULL;
			head=temp;
			print();
			
		}
		void delI(int* x){
			Node* temp=head;
			int i=1;
			while(i<*x && temp!=NULL){
				temp=temp->Rnode;	
				i++;
			}
			temp->Rnode=temp->Rnode->Rnode;
			temp->Rnode->Rnode->Lnode=temp;	
		}
		void delend(){
			Node* temp=head;
			Node* llink=head;
			while(temp->Rnode!=NULL){
				if(temp->Rnode->Rnode==NULL){
					temp=llink->Rnode;
					llink->Rnode=temp->Rnode;
				}
			}
			
		}
		void deleteelement(){
			cout<<"Where do you wish to delete the elements?"<<endl;
			cout<<"\t1.Begining"<<endl;
			cout<<"\t2.Given postiion"<<endl;
			cout<<"\t3.End"<<endl;
			int choice;
			cin>>choice;
			switch(choice){
				case 1:
					delbegin();
					break;
				case 2:
					int pos;
					cout<<"\nEnter position"<<endl;
					cin>>pos;
					//delI(&pos);
					break;
				case 3:
					delend();
					break;
			} 
		}
		//to print the elements in the linked list
		void print(){
			Node* temp=head;
			while(temp!=NULL){
				cout<<"\t"<<temp->data;
				temp=temp->Rnode;
			}
		}
		void option(){
			int x=1;
			while(x!=0){
				cout<<"\nEnter the Option:"<<endl;
				cout<<"\t1.Insert Element in LL"<<endl;
				cout<<"\t2.Delete Element in LL "<<endl;
				cout<<"\t3.Print Elements in LL"<<endl;
				cout<<"\t4.Exit"<<endl;
				int opt;
				cin>>opt;
				switch(opt){
					case 1:
						insertelement();
						break;
					case 2:
						deleteelement();
						break;
					case 3:
						print();
						break;
					case 4:
						exit(0);
					}
			}
		}
			
};
int main(){
	dllist dll;
	dll.option();
}
