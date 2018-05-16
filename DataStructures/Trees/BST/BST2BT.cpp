//Convert A BST to Binary tree by adding all the numbers
#include<iostream>
using namespace std;
class BinSTree{
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
	void printInorder(Node *root){
		if(root!=NULL){	
			printInorder(root->left);
			cout<<root->data<<" ";
			printInorder(root->right);
		}
	}
	void BST2BT(Node *root, int *sum){
		if(root==NULL) return;
		else{
			
			BST2BT(root->right,sum);
			cout<<"\nroot->data "<<root->data<<endl;
			*sum+=root->data;
			root->data=*sum;
			cout<<"Sum "<<*sum<<endl;
			BST2BT(root->left,sum);
			
		}
	}
	public:
	void driver(){
		Node * root=new Node();
		root=NULL;
		int sum=0;
		root=insertNode(root,5);
		root=insertNode(root,2);
		root=insertNode(root,13);
		root=insertNode(root,1);
		root=insertNode(root,0);
		printInorder(root);
		BST2BT(root,&sum);
		cout<<endl;
		printInorder(root);
	}
};
int main(){
	BinSTree bst;
	bst.driver();
}

