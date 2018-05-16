//Delete a Bin Tree
#include<iostream>
#include<stdlib.h>
using namespace std;
class BinTree{
	public:
		struct Node{
			int data;
			Node *left,*right;
		};
		Node *newNode(int data){
			Node *temp=new Node();
			temp->data=data;
			temp->left=temp->right=NULL;
			return temp;
		}
		
		//Method to delete tree in a non recursive way
		void NonRecursiveDeleteBinTree(Node *root){
			if (root==NULL) return;
			queue<Node *> q;
			Node *current;
			current=root;
			q.push(root);
			while(!q.empty()){
				Node *node=q.front();
				q.pop();
				if (node->left!=NULL){
					q.push(node->left);
				}
				if(node->right!=NULL){
					q.push(node->right);
				}
				free(node);
			}
		}
		
		//Recursive way to delete a tree
		void RecursiveDeleteBinTree(Node *root){
			if (root==NULL){
				return;
			}
			deleteBinTree(root->left);
			deleteBinTree(root->right);
			cout<<root->data<<" ";
			free(root); return;
		}
		
		void print(Node *root){
			if(root==NULL){
				return;
			}
			print(root->left);
			cout<<root->data<<" ";
			print(root->right);
		}
		
		void operate(){
			Node *root=newNode(1);
			root->left=newNode(2);
			root->right=newNode(3);
			root->left->left=newNode(4);
			root->left->right=newNode(5);
			root->right->left=newNode(6);
			root->right->right=newNode(7);
			print(root);
			cout<<endl;
			RecursiveDeleteBinTree(root);
			cout<<endl;
			if(root!=NULL){
				print(root);
			}else{
				cout<<"Deleted!";
			}

		}
};
int main(){
	BinTree bt;
	bt.operate();
}
