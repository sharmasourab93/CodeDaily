//Print Ancestors
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
		//Printing all the ancestors in a tree from the target node
		bool printAncestors(Node * root, int target){
			if(root==NULL) return false;
			if(root->data==target) return true;
			if(printAncestors(root->left, target)||printAncestors(root->right,target)){
				cout<<root->data<<" ";
				return true;
			}
			return false;
		}
		void driver(){
			Node * root=newNode(1);
			root->left=newNode(2);
			root->right=newNode(3);
			root->left->right=newNode(4);
			root->left->left=newNode(5);
			root->left->left->left=newNode(6);
			cout<<printAncestors(root,7);
		}
};
int main(){
	BinTree bt;
	bt.driver();
}
