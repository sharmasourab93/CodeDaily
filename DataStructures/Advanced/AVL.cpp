#include<iostream>
#include<stdlib.h>
using namespace std;
struct Node{
	int key;
	Node *left;
	Node *right;
	int height;
};
int max(int a,int b){ return ((a>b)?a:b);}
int height(Node *N){
	if(N==NULL) return 0;
	return N->height;
}
Node* newNode(int key){
	Node* node=new Node();
	node->key=key;
	node->left=NULL;
	node->right=NULL;
	node->height=1;
	return(node);
}
Node *rightRotate(Node *y){
	Node *x=y->left;
	Node *T2=x->right;
	
	x->right=y;
	y->left=T2;
	
	y->height=max(height(y->left),height(y->right))+1;
	x->height=max(height(x->left),height(x->right))+1;
	
	return x;
}
Node *leftRotate(Node *y){
	Node *x=y->left;
	Node *T2=x->right;
	
	x->right=y;
	y->left=T2;
	
	x->height=max(height(x->left),height(x->right))+1;
	y->height=max(height(y->left),height(y->right))+1;
	
	return y;
}
int getBalance(Node *N){
	if(N==NULL) return 0;
	return height(N->left)-height(N->right);
}
Node *insert(Node* node,int key){
	//Perform the normal BST Insertion
	if(node==NULL) return (newNode(key));
	if(key<node->key) node->left=insert(node->left,key);
	else if(key>node->key) node->right=insert(node->right,key);
	else return node;
	
	//Update Height of this ancestor node
	node->height=1+max(height(node->left),height(node->right));
	//Get the balance factor of this ancestor node to check whether this node became unbalanced
	int balance=getBalance(node);
	//if this node becomes unbalanced then there are 4 cases
	//Left left case
	if(balance>1 &&key<node->left->key) return rightRotate(node);
	//Right Right case
	if(balance<-1 &&key>node->right->key) return rightRotate(node);
	//Left right case
	if(balance>1 && key>node->left->key){
		node->left=leftRotate(node->left);
		return rightRotate(node);
	}
	//Right Left case
	if(balance<-1 && key<node->right->key){
		node->right=rightRotate(node->right);
		return leftRotate(node);
	}
	//Return the unchanged Node Pointer
	return node;
}
//Performing Deletion of Nodes in AVL
Node * deleteNode(Node * root, int key){
	if(root==NULL) return root; 
	if(key<root->key)
		root->left=deleteNode(root->left, key);
		
	else if(key>root->key)
		root->right=deleteNode(root->right,key);
	else{
		if((root->left==NULL)|| (root->right==NULL)){
			Node *temp=root->left?root->left:root->right;
			if(temp==NULL){
				temp=rrot;
				root=NULL;
			}
			else{
				
				*root=*temp;
				free(temp);
			}
		}else{
			Node* temp=minValueNode(root->right);
			root->key=temp->key;
			root->right=deleteNode(root->right, temp->key);
		}
	}
	//--------------BST procedure ends here
	if(root==NULL) return root; 
	root->height=1+max(height(root->left),height(root->right));
	int balance=getBalance(root);
	//Left Left Case
	if(balance>1 && getBalance(root->left)>=0) return rightRotate(root);
	//Left Right case
	if(balance>1 && getBalance(root->right)<0){
		root->left=leftRotate(root->left);
		return rightRotate(root);
	}
	//Right Right case
	if(balance<-1 && getBalance(root->right)<=0) return leftRotate(root);
	//Right left case
	if(balance<-1 && getBalance(root->right)>0){
		root->right=rightRotate(root->right);
		return leftRotate(root);
	}
	return root
}
void preOrder(Node *root){
	if(root!=NULL){
		cout<<root->key<<" ";
		preOrder(root->left);
		preOrder(root->right);
	}
}
int main(){
	Node *root=NULL;
	root=insert(root,10);
	root=insert(root,20);
	root=insert(root,30);
	root=insert(root,40);
	root=insert(root,50);
	root=insert(root,25);
	cout<<"\nPreorder traversal of the constructed AVL tree is: "<<endl;
	preOrder(root);
	return 0;
}
