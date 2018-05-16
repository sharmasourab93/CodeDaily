//Lowest common Ancestors 
#include<iostream>
using namespace std;
class BinTree{
	public:
		//Defines the structure of the node in a tree
		struct Node{
			int data;
			Node *left, *right;
		};
		//Creates/adds new nodes to the tree
		Node * newNode(int data){
			Node * temp=new Node();
			temp->data=data;
			temp->left=NULL;
			temp->right=NULL;
			return temp;
		}
		//Lowest Common Ancestor
		Node *LCA(Node * root,int tar1, int tar2){
			if(root==NULL) return NULL;
			if(root->data==tar1||root->data==tar2) return root;
			Node *left=LCA(root->left,tar1,tar2);
			Node *right=LCA(root->right,tar1,tar2);
			if(left && right) return root;
			return ((left!=NULL)?left:right);
		}
		//Primary driver function 
		void driver(){
			Node * root=newNode(1);
			root->left=newNode(2);
			root->right=newNode(3);
			root->left->right=newNode(4);
			root->left->left=newNode(5);
			root->left->left->left=newNode(6);
			cout<<LCA(root,6,4)->data<<endl;
			cout<<LCA(root,2,4)->data<<endl;
			cout<<LCA(root,3,4)->data<<endl;
		}
};
int main(){
	BinTree bt;
	bt.driver();
}
