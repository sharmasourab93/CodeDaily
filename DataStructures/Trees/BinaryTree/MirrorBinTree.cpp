//An Efficient function to convert a Binary tree
//into its Mirror
#include<iostream>
using namespace std;
class BinTree{
	public:
		struct Node{
			int data;
			Node *left, *right;
		};
		Node * newNode(int data){
			Node * temp=new Node();
			temp->data=data;
			temp->left=NULL;
			temp->right=NULL;
			return temp;
		}
		Node* Mirror(Node * root){
			if(root==NULL) return NULL;
			Node * mirror = new Node();
			mirror->data = root-> data;
			mirror->left=Mirror(root->right);
			mirror->right=Mirror(root->left);
			return mirror;
		}
		//Prints the tree inorder
		void printInorder(Node *root){
			if(root==NULL) return;
			printInorder(root->left);
			cout<<root->data<<" ";
			printInorder(root->right);
		}
		//primary driver function
		void driver(){
			Node * root=newNode(1);
			root->left=newNode(3);
			root->right=newNode(2);
			root->right->right=newNode(4);
			root->right->left=newNode(5);
			printInorder(root);
			cout<<endl;
			Node * mirror=new Node();
			mirror->left=NULL;
			mirror->right=NULL;
			mirror=Mirror(root);
			printInorder(mirror);
		}
		
};
int main(){
	BinTree bt;
	bt.driver();
}
