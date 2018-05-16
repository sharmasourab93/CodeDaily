//Finding range
#include<iostream>
using namespace std;
class BinSTree{
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
		//Inserts node into the BST wrt BST Properties
		Node * insertNode(Node * root,int data){
			if(root==NULL) return newNode(data);
			if(root->data<data) 
				root->right=insertNode(root->right,data);
			else if(root->data>data) 
				root->left=insertNode(root->left,data);
		}
		bool inRange(Node *root,int min, int max){
			return root->data>=min && root->data<=max;
		}
		static int count;
		bool countNodesinRange(Node *root,int min,int max){
			if(root==NULL) return true;
			bool l=(root->left)? countNodesinRange(root->left,min,max) : true;
			bool r=(root->right)? countNodesinRange(root->right,min,max) : true;
			if(l&&r&&inRange(root,min,max)){
				++count;
				return true;
			}
			return false;
		}
		void driver(){
		    Node *root = NULL;
		    root = insertNode(root, 50);
		    insertNode(root, 30);
		    insertNode(root, 20);
		    insertNode(root, 40);
		    insertNode(root, 70);
		    insertNode(root, 60);
		    insertNode(root, 80);
		    bool j=countNodesinRange(root,5,45);
		    cout<<j<<" "<<count;
		    
		}
};
int main(){
	BinSTree bst;
	bst.driver();
}
