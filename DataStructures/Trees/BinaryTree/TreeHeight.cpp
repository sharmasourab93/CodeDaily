/*Program to find the Maximum depth or height of a Tree*/
#include<iostream>
using namespace std;
class TreeHeight{
	public:
		struct Node{
			int data;
			Node* left;
			Node* right;
		};
		Node *newNode(int data){
			Node *temp=new Node();
			temp->data=data;
			temp->left=temp->right=NULL;
		}
		int max(int x, int y){
			return ((x>y)?x:y);
		}
		int calcHeight(Node *root){
			int h;
			if (root==NULL) return 0;
			int l=1+calcHeight(root->left);
			int r=1+calcHeight(root->right);
			return max(l,r);
		}
		void driver(){
			Node * root=newNode(1);
			root->left=newNode(2);
			root->right=newNode(3);
			root->left->right=newNode(4);
			root->left->left=newNode(5);
			root->left->left->left=newNode(6);
			int h=calcHeight(root);
			cout<<h<<endl;
		}
};
int main(){
	TreeHeight th;
	th.driver();
}
