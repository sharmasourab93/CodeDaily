/*Program to Check if a given tree is a BST or not*/
//Self implemented but failed
#include<iostream>
#include<stdlib.h>
using namespace std;
class BSTorNot{
	public: 
		struct Node{
			int data;
			Node* left;
			Node* right;
		};
		//Node* Point=new Node();
		struct Node* newNode(Node* node,int key){
			Node* temp=new Node();
			temp=node;
			temp->data=key;
			temp->left=temp->right=NULL;
			return temp;
		}
		struct Node* insert(Node* node,int key){
			if(node==NULL){
				return newNode(node,key);
			}
			node->left=insert(node->left,30);
			node->right=insert(node->right,10);
			node->left->left=insert(node->left->left,5);
			node->left->right=insert(node->left->right,6);
		}
		void inorder(Node* node){
			if(node==NULL) return ;
			inorder(node->left);
			cout<<node->data<<"\t";
			inorder(node->right);
		}
		void BSTCheck(Node* root,Node *l=NULL,Node *r=NULL){
			if(root==NULL) return true;
			if(l!=NULL && root->data<l->data) return false;
			if(r!=NULL && root->data>r->data) return false;
			return isBST(root->left,l,root) && isBST(root->right,root,r);
		}
		int m(){
			Node *Point=insert(Point,20);
			cout<<"Inorder: "<<endl;
			inorder(Point);
			cout<<"BST Test: "<<endl;
			BSTCheck(Point);
			
		}
};
int main(){
	BSTorNot bn;
	bn.m();
}
