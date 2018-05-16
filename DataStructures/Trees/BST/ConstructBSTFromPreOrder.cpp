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


		void driver(){

			/*
			Node *root = insertNode(root, 50);
		    insertNode(root, 30);
		    insertNode(root, 20);
		    insertNode(root, 40);
		    insertNode(root, 70);
		    insertNode(root, 60);
		    insertNode(root, 80);
		    inorder(root);*/

		    int pre[]={10,5,1,7,40,50};

		    
		}
}
int main(){

}