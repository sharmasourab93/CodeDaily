//Diameter of a binary tree
#include<iostream>
using namespace std;
class BinTree{
	public:
		struct Node{
			int data;
			Node *left, *right;
		};
		int max(int a, int b){
			return ((a>b)?a:b);
		}
		Node * newNode(int data){
			Node * temp=new Node();
			temp->data=data;
			temp->left=NULL;
			temp->right=NULL;
			return temp;
		}	
		int height(Node * root){
			if(root==NULL) return 0;
			int m;
			int lheight=1+(height(root->left));
			int rheight=1+(height(root->right));
			m=max(lheight,rheight);
			return m;
		}
		int diameter(Node *tree){
			if(tree==NULL) return 0;
			int lheight=height(tree->left);
			int rheight=height(tree->right);
			
			int ldiameter=diameter(tree->left);
			int rdiameter=diameter(tree->right);
			
			return max((lheight+rheight+1),max(ldiameter,rdiameter));
		}
		void driver(){
			Node * root=newNode(1);
			root->left=newNode(2);
			root->right=newNode(3);
			root->left->right=newNode(4);
			root->left->left=newNode(5);
			//root->left->left->left=newNode(6);
			cout<<"\nHeight of tree "<<height(root)<<endl;//<<x<<endl;
			cout<<"\nDiameter of a tree "<<diameter(root)<<endl;
		}
};
int main(){
	BinTree bt;
	bt.driver();
}
