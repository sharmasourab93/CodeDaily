//Implementation of Tree Traversals 
#include<iostream>
using namespace std;
struct Node{
	int data;
	Node *left;
	Node *right;
};

Node *newNode(int data){
	Node *temp=new Node();
	temp->data=data;
	temp->left=temp->right=NULL;
	return temp;
}

//Inorder Traversal Left Root Right
void InOrder(Node *root){
	if(root==NULL)return;
	InOrder(root->left);
	cout<<root->data<<" ";
	InOrder(root->right);
}	

//Preorder Traversal Root Left Right
void PreOrder(Node *root){
	if(root==NULL)return ;
	cout<<" "<<root->data;
	PreOrder(root->left);
	PreOrder(root->right);
}	

//Post Order Traversal Left Right Root
void PostOrder(Node *root){
	if(root==NULL)return;
	PostOrder(root->left);
	PostOrder(root->right);
	cout<<" "<<root->data;
}

int main(){
	Node *root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
    root->right->left = newNode(6);
    root->right->right = newNode(7);
    root->right->left->right = newNode(8);
    root->right->right->right = newNode(9);

    cout<<"Inorder Traversal:"<<endl;
    InOrder(root);
    cout<<"\nPreorder Traversal:"<<endl;
    PreOrder(root);
    cout<<"\nPostorder Traversal:"<<endl;
    PostOrder(root);
    cout<<endl;
}
