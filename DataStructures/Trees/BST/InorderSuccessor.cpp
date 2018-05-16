//Inorder Successor 
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
		Node *minValueNode(Node *root){
			if(root==NULL) return NULL;
			while(root->left){
				root=root->left;
			}
			return root;
		}
		//Find successor
		Node* findSuc(Node *root,Node *temp){
			if(temp->right!=NULL){
				return minValueNode(temp->right);
			}
			Node *suc=NULL;
			while(root!=NULL){
				if(temp->data<root->data){
					suc=root;
					root=root->left;
				}
				else if(temp->data>root->data){
					root=root->left;
				}
				else break;
			}
			return suc;
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
		    Node *tmp=root->left->right;
		    Node *suc=findSuc(root,tmp);
		    if(suc!=NULL) cout<<"\nSuccessor found!: "<<suc->data<<endl;
		    else cout<<"\nNo successor Found\n"<<endl;
		}
};
int main(){
	BinSTree bst;
	bst.driver();
}
