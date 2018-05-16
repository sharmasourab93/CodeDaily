#include<iostream>
using namespace std;

class BST{
	public:
		struct Node {
			int data;
			Node *left,*right;
		};
		Node *newNode(int data){
			Node * newnode=new Node();
			newnode->data=data;
			newnode->left=newnode->right=NULL;
			return newnode;
		}

		Node * insertNode(Node * root,int data){
			if(root==NULL) return newNode(data);
			if(root->data<data) 
				root->right=insertNode(root->right,data);
			else if(root->data>data) 
				root->left=insertNode(root->left,data);
		}

		Node *lca(Node *root, int n1, int n2){
			if(root==NULL) return NULL;
			if(root->data>n1 && root->data>n2){
				return lca(root->left,n1,n2);
			}
			if(root->data<n1 && root->data<n2){
				return lca(root->right,n1,n2);
			}
			return root;
		}

		void inorder(Node *root){
			if(root==NULL) return;
			inorder(root->left);
			cout<<root->data<<" ";
			inorder(root->right);
		}

		void driver(){
			Node *root = insertNode(root, 50);
		    insertNode(root, 30);
		    insertNode(root, 20);
		    insertNode(root, 40);
		    insertNode(root, 70);
		    insertNode(root, 60);
		    insertNode(root, 80);
		    inorder(root);
		}

};
int main(){
	BST bst;
	bst.driver();
}