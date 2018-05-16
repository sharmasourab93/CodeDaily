/*Program for a basic Binary Search Tree*/
#include<iostream>
#include<stdlib.h>
using namespace std;
class BST{
	public:
		//Structure of the New Node
		struct Node{
			int data;
			Node* left;
			Node* right;
		};
		//Inserts New Node
		struct Node* newNode(int item){
			struct Node *temp=new Node();
			temp->data=item;
			temp->left=temp->right=NULL;
			return temp;
		};
		
		//Insert Node Function
		struct Node* insert(Node* node, int data){
			/*If the tree is empty, return a new node*/
			if(node==NULL) return newNode(data);
			/*Otherwise, recur down the tree*/
			if(data<node->data)
				node->left=insert(node->left,data);
			else if(data>node->data)
				node->right=insert(node->right,data);
			return node;
		}
		
		//Delete Value
		struct Node* deleteNode(Node* node,int data){
			if(node==NULL){
				return node;
			}
			if(data<node->data){
				node->left=deleteNode(node->left,data);
			}else if(data>node->data){
				node->right=deleteNode(node->right,data);
			}
			else{
				if(node->left==NULL){
					Node* temp=node->right;
					free(node);
					return temp;
				}else if(node->right==NULL){
					Node* temp=node->left;
					free(node);
					return temp;
				}
				Node* temp=minValue(node->right);
				node->data=temp->data;
				node->right=deleteNode(node->right,temp->data);
			}
			return node;
		}
		
		//Min Value
		struct Node* minValue(Node* node){
			Node* current=node;
			while(current->left!=NULL){
				current=current->left;
			}
			return current;
		}
		
		//Prints in Inorder Method
		void inorder(Node* node){
			if(node!=NULL)
			{
				inorder(node->left);
				cout<<(node->data)<<"\t";
				inorder(node->right);
			}
		}
		
		int m(){
			Node *root=NULL;
			root=insert(root,50);
			insert(root,30);
			insert(root,20);
			insert(root,40);
			insert(root,70);
			insert(root,60);
			insert(root,80);
			cout<<"\nInorder Traversal:"<<endl;
			inorder(root);
			cout<<"\nDelete 20"<<endl;
			root=deleteNode(root,20);
			inorder(root);
			cout<<"\nDelete 30"<<endl;
			root=deleteNode(root,30);
			inorder(root);
			cout<<"\nDelete 50"<<endl;
			root=deleteNode(root,50);
			inorder(root);
			
			return 0;
		}
};
int main(){
	BST bst;
	bst.m();
}
