//Linked list to Binary Search tree
#include<iostream>
using namespace std;
class BinSTree{
	public:
		//Node's Structure
		struct Node{
			Node * left,*right;
			int data;
		};
		//Inserts new node into the data
		Node *newNode(int data){
			Node * newnode=new Node();
			newnode->data=data;
			newnode->left=newnode->right=NULL;
			return newnode;
		}
		//Inserts node into the BST wrt BST Properties
		Node *insertNode(Node *root,int data){
			if(root==NULL) return newNode(data);
			if(root->data<data) 
				root->right=insertNode(root->right,data);
			else if(root->data>data) 
				root->left=insertNode(root->left,data);
		}
		//Pushes node into the linked List
		void pushNode(Node * root, int data){
			Node *node=new Node();
			node->data=data;
			node->left=NULL;
			node->right=root;
			root=node;
			//return root;
		}
		void appendNode(Node * root, int data){
			if(root==NULL) root=newNode(data);
			else{
				Node *node=new Node();
				node->data=data;
				node->left=NULL;
				node->right=NULL;
				//Node *node1=new Node();
				//node1=root;
				while(root->right!=NULL){
					root=root->right;
				}
				root->right=node;
			}
		}
		//Returns the linear index of the LinkedList
		int sizeofList(Node *root){
			Node * temp=new Node();
			temp=root;
			int count=0;
			while(temp!=NULL){
				temp=temp->right;
				++count;
			}
			return count;
		}
		void printNode(Node* root){
			if(root==NULL) return;
			cout<<"Printing Data in Nodes linearly"<<endl;
			while(root!=NULL){
				cout<<root->data<<" ";
				root=root->right;
			}
		}
		Node *traverse(Node * root, int data){
			Node * temp1=new Node();
			Node *temp2=new Node();
			temp1=root;
			for(int i=0;i<data;i++){
				temp1=temp1->right;
			}
			temp2=temp1->right;
			temp2->right=NULL;
			return newNode(temp2->right->data);
		}
		Node *convert(Node * root,int start, int end){
			if(root==NULL) return NULL;
			Node * temp=new Node();
			temp=root;
			if(start>end){
				int mid=(start+end)/2;
				temp=traverse(root,mid);
				temp->left=convert(root,start,mid-1);
				temp->right=convert(root,mid+1,end);
			}
			return temp;
			
		}
		void printpreorder(Node *root){
			if(root!=NULL){	
				
				printpreorder(root->left);
				cout<<root->data<<" ";
				printpreorder(root->right);
				
			}
		}
		void driver(){
			Node *root=new Node();
			appendNode(root,1);
			appendNode(root,2);
			appendNode(root,3);
			appendNode(root,4);
			appendNode(root,5);
			printNode(root);
			int end=sizeofList(root);
			cout<<"\nSize of the list "<<end<<endl;
			Node *bstroot=new Node();
			bstroot=convert(root,0,end);
			printpreorder(bstroot);
		}
};
int main(){
	BinSTree bst;
	bst.driver();
}
