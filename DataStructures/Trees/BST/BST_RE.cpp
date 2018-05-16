//Binary Search Tree 
#include<iostream>
#include<stdlib.h>
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
		//Returns the node in which the key is given
		Node * search(Node * root, int key){
			if(root==NULL||root->data==key) return root;
			if(root->data<key) return search(root->right,key);
			else if(root->data>key) return search(root->left,key);
		}
		
		Node * minValueNode(Node * root){
			Node * current=new Node();
			current=root;
			while(current->left!=NULL)
				current=current->left;
			return current;
		}
		void printInorder(Node *root){
			if(root!=NULL){	
				printInorder(root->left);
				cout<<root->data<<" ";
				printInorder(root->right);
			}
		}
		//Deletes a node in the BST
		Node * delNode(Node * root,int key){
			//Base Case
			if(root==NULL)
				 return root;
			//Shifting to left if the key is smaller than the root
			if(root->data>key)
				 root->left=delNode(root->left,key);
			//Shifting to the right if the key is greater than the root
			else if(root->data<key)
				 root->right=delNode(root->right,key);
			//If the code gets to this point
			//This is where the node has to be deleted
			else{
				// If a node has only one child
				if(root->left==NULL){
					Node * temp=root->right;
					free(root);
					return temp;
				}else if(root->right==NULL){
					Node * temp=root->left;
					free(root);
					return temp;
				}
				//If the node has two children
				Node * temp=minValueNode(root->right);
				root->data=temp->data;
				root->right=delNode(root->right,temp->data);
			}
			return root;
		}
		void driver(){
		    Node *root=NULL;
			root=insertNode(root,50);
			insertNode(root,30);
			insertNode(root,20);
			insertNode(root,40);
			insertNode(root,70);
			insertNode(root,60);
			insertNode(root,80);
			//cout<<root->left->data<<endl;
			cout<<"\nInorder Traversal:"<<endl;
			printInorder(root);
			cout<<"\nDelete 20"<<endl;
			root=delNode(root,20);
			printInorder(root);
			cout<<"\nDelete 30"<<endl;
			root=delNode(root,30);
			printInorder(root);
			cout<<"\nDelete 50"<<endl;
			root=delNode(root,50);
			printInorder(root);
		}
		
};
int main(){
	BinSTree bst;
	bst.driver();
}
