//K-th Smallest element in a BST
#include<iostream>
#include<stack>
using namespace std;
	static int l=0;
	static int res=0;
class BinSTree{

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
		Node *insertNode(Node * root,int data){
			if(root==NULL) return newNode(data);
			if(root->data<data) 
				root->right=insertNode(root->right,data);
			else if(root->data>data) 
				root->left=insertNode(root->left,data);
		}
		void countK(Node *root, int k){
			stack<int> s;
			if(root!=NULL && l<=k){
				countK(root->left,k);
				l++;
				if(l==k){
					cout<<"root data :" << root->data <<endl;
					res =root->data;
				}
				countK(root->right,k);
			}
		}
		Node * minValueNode(Node * root){
			Node * current=new Node();
			current=root;
			while(current->left!=NULL)
				current=current->left;
			return current;
		}
		void printInorder(Node *root){
			if(root!=NULL){	
				printInorder(root->left);
				cout<<root->data<<" ";
				printInorder(root->right);
			}
		}
		void driver(){
		    Node *root=NULL;
			root=insertNode(root,50);
			insertNode(root,30);
			insertNode(root,20);
			insertNode(root,40);
			insertNode(root,70);
			insertNode(root,60);
			insertNode(root,80);
			cout<<"\nInorder Traversal:"<<endl;
			printInorder(root);
			int k=3;
			countK(root,k);
			cout<<k<<"th Smallest Element is: "<<res<<endl;
		}	
};
int main(){
	BinSTree bst;
	bst.driver();
}
