#include<iostream>
using namespace std;
class BinTree{
	public:
		struct Node{
			int data;
			Node *left,*right;
		};
		Node *newNode(int data){
			Node *temp=new Node();
			temp->data=data;
			temp->left=temp->right=NULL;
			return temp;
		}

		Node *findLCA(Node *root,int n1,int n2){
			if(root==NULL) return NULL;
			if(root->data==n1||root->data==n2) return root;

			Node *left=findLCA(root->left,n1,n2);
			Node *right=findLCA(root->right,n1,n2);

			if(left && right) return root;

			return (left!=NULL?left: right);
		}

		bool printAncestors(Node *root, int t1){
			if(root==NULL) return false;
			if(root->data==t1){
				cout<<root->data<<" ";
				return true;
			}
			if(printAncestors(root->left,t1)||printAncestors(root->right,t1)){
				cout<<root->data<<" ";
				return true;
			}
			return false;
		}

		bool findCommonNodes(Node *root, int first, int second){
			Node *LCA=findLCA(root,first,second);
			if(LCA==NULL){
				return false;
			}
			printAncestors(root,LCA->data);
		}

		void operate(){
			Node* root = newNode(1);
    		root->left = newNode(2);
    		root->right = newNode(3);
    		root->left->left = newNode(4);
    		root->left->right = newNode(5);
    		root->right->left = newNode(6);
    		root->right->right = newNode(7);
    		root->left->left->left = newNode(8);
    		root->right->left->left = newNode(9);
    		root->right->left->right = newNode(10);
 
			if(findCommonNodes(root,6,7)==false){
				cout<<"No common Nodes";
			}

		}
};

int main(){
	BinTree bt;
	bt.operate();
}