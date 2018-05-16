//Is a Binary tree height balanced?
#include<iostream>
#include<math.h>
using namespace std;
class BinTree{
	public:
		struct Node{
			int data;
			Node *left,*right;
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
		bool checkBalanced(Node * root){
			if(root==NULL) return 1;
			int lh=height(root->left),rh=height(root->right);
			if(abs(lh-rh)<=1&&checkBalanced(root->left)&&checkBalanced(root->right))
				return 1;
			return 0;
		}
		void driver(){
			Node * root=newNode(1);
			root->left=newNode(2);
			root->right=newNode(3);
			root->left->right=newNode(4);
			root->left->left=newNode(5);
			root->left->left->left=newNode(6);
			cout<<"\nHeight of tree "<<height(root)<<endl;
			if(checkBalanced(root)){cout<<"\nBalanced Tree"<<endl; return;}
			else{cout<<"\nNot a balanced tree"<<endl; return;}
		}
		
};
int main(){
	BinTree bt;
	bt.driver();
}
