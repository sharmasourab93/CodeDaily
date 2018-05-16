//Root to leaf path sum equal to a given number
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
		bool findSum(Node *root, int sum){
			if(root==NULL) return sum==0;
			else{
				bool ans=0;
				int subSum=sum-root->data;
				if(subSum==0 &&root->left==NULL && root->right==NULL){
					return 1;
				}
				if(root->left) ans=ans||findSum(root->left,sum);
				if(root->right) ans=ans||findSum(root->right,sum);
				return ans;
			}
		}
		void driver(){
			Node * root=newNode(1);
			root->left=newNode(2);
			root->right=newNode(3);
			root->left->right=newNode(4);
			root->left->left=newNode(5);
			root->left->left->left=newNode(6);
			cout<<findSum(root,7);
		}
		
};
int main(){
	BinTree bt;
	bt.driver();
}
