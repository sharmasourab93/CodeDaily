//Morris Traversal for Preorder
#include<iostream>
#include<stdlib.h>
using namespace std;
class Morris{
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
		//An Inorder Traversal without using Recursion or stack 
		void MorrisInorderTraversal(Node *root){
			Node *current,*pre;
			if(root==NULL) return;
			current=root;
			while(current!=NULL){
				if(current->left==NULL){
					cout<<current->data<<" ";
					current=current->right;
				}
				else{
					pre=current->left;
					while(pre->right!=NULL && pre->right!=current){
						pre=pre->right;
					}
					if(pre->right==NULL){
						pre->right=current;
						current=current->left;
					}
					else{
						pre->right=NULL;
						cout<<current->data<<" ";
						current=current->right;
					}
				}
			}
		}
		//A Traversal without using Recursion or stack
		void MorrisPreorderTraversal(Node *root){
			while(root){
				if(root->left==NULL){
					cout<<root->data<<" ";
					root=root->right;
				}else{
					Node *current=root->left;
					while(current->right && current->right!=root){
						current=current->right;
					}
					if(current->right==root){
						current->right=NULL;
						root=root->right;
					}else{
						cout<<root->data<<" ";
						current->right=root;
						root=root->left;
					}
				}
			}
		}
		void operate(){
			Node * root=newNode(1);
			root->left=newNode(2);
			root->right=newNode(3);
			root->left->right=newNode(4);
			root->left->left=newNode(5);
			root->left->left->left=newNode(6);
			cout<<"\nMorris Preorder Traversal:"<<endl;
			MorrisPreorderTraversal(root);
			cout<<"\nMorris Inorder Traversal"<<endl;
			MorrisInorderTraversal(root);
			cout<<endl;
		}
};
int main(){
	Morris m;
	m.operate();
}