//Kth Largest element in a list
#include<iostream>
using namespace std;
class BinSTree{
	static int count;
	public:
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
		//Prints in Inorder
		void printInorder(Node *root){
			if(root!=NULL){	
				printInorder(root->left);
				cout<<root->data<<" ";
				printInorder(root->right);
			}
		}
		//Kth Largest element
		void findLarge(Node *root, int k){
			if(root==NULL && count>2) return;
			if(count<=k){
				findLarge(root->right,k);
				++count;
				if(count==k){
					cout<<root->data<<endl;
				}
				findLarge(root->left,k);
			}
		}
		void driver(){
			Node * root=new Node();
			root=insertNode(root,10);
			insertNode(root,15);
			insertNode(root,7);
			insertNode(root,3);
			insertNode(root,13);
			insertNode(root,25);
			cout<<"\nPrinting in Inorder"<<endl;
			printInorder(root);
			cout<<"\n"<<root->left->data<<endl;
			int k=2;
			cout<<"\nThe "<<k<<"th largest element is: "<<endl;
			findLarge(root,2);
		}
};
int main(){
	BinSTree bst;
	bst.driver();
}
