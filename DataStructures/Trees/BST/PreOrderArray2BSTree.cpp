//Construct BST from  a given preorder traversal
#include<iostream>
using namespace std;
class BinSTree{
	public:
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
		Node * insertNode(Node * root,int data){
			if(root==NULL) return newNode(data);
			if(root->data<data) 
				root->right=insertNode(root->right,data);
			else if(root->data>data) 
				root->left=insertNode(root->left,data);
		}
		void printInorder(Node *root){
			if(root!=NULL){	
				printInorder(root->left);
				cout<<root->data<<" ";
				printInorder(root->right);
			}
		}
		void printPreorder(Node *root){
			if(root!=NULL){	
				cout<<root->data<<" ";
				printPreorder(root->left);
				printPreorder(root->right);
			}
		} 
		Node *constructTree(int *array, int size){
			Node * root=NULL;//new Node();
			for(int i=0;i<size;i++){
				root=insertNode(root,array[i]);
			}
			//printPreorder(root);
			cout<<endl;
			return root;
		}
		int driver(){
			int preOrder[]={100,10,20,15,11,50,31,150,200};
			//int preOrder[]={100,10,20,15,50,31,11,200};
			int size=sizeof(preOrder)/sizeof(preOrder[0]);
			Node * root;//=new Node();
			root=constructTree(preOrder,size);
			cout<<"\nInorder"<<endl;
			printInorder(root);
			cout<<"\nPreorder"<<endl;
			printPreorder(root);
			
		}
};
int main(){
	BinSTree bst;
	bst.driver();
}
