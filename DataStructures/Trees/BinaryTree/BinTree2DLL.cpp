//A Binary Tree to a Doubly Linked List 
#include<iostream>
using namespace std;
class BinTree{
	public:
		struct Node{
			int data;
			Node* left;
			Node* right;
		};
		Node *newNode(int data){
			Node *temp=new Node();
			temp->data=data;
			temp->left=temp->right=NULL;
		}
		
		Node *BT2DLL(Node *root){
			if (root==NULL) return root;
			if(root->left!=NULL){
				Node *left=BT2DLL(root->left);
				while(left->right!=NULL){
					left=left->right;
				}
				left->right=root;
				root->left=left;
			}
			if(root->right!=NULL){
				Node *right=BT2DLL(root->right);
				while(root->right!=NULL){
					right=right->left;
				}
				right->left=root;
				root->right=right;
			}
			return root;
		}
		
		Node *bintree2dllist(Node *root){
			if(root==NULL) return root;
			root=BT2DLL(root);
			while(root->left!=NULL){
				root=root->left;
			}
			return root;
		}
		void printDLL(Node *root){
			Node *temp=root;
			while(temp!=NULL){
				cout<<temp->data<<" ";
				temp=temp->right;
			}
		}
		void driver(){
			Node * root=newNode(1);
			root->left=newNode(2);
			root->right=newNode(3);
			root->left->right=newNode(4);
			root->left->left=newNode(5);
			root->left->left->left=newNode(6);
			Node *head=bintree2dllist(root);
			printDLL(head);
		}
};
int main(){
	BinTree bt;
	bt.driver();
}
