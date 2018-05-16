//InOrder Predecessor Successor 
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
		//Finding predecessor and Successor
		void findPreSuc(Node *root, Node*& pre,Node *&suc, int key){
			if(root==NULL) return;
			if(root->data==key){
				if(root->left!=NULL){
					Node *tmp=root->left;
					while(tmp->right)
						tmp=tmp->right;
					pre=tmp;
				}
				if(root->right!=NULL){
					Node *tmp=root->right;
					while(tmp->left){
						tmp=tmp->left;
					}
					suc=tmp;
				}
				return;
			}
			if(root->data>key){
				suc=root;
				findPreSuc(root->left,pre,suc,key);
			}else{
				pre=root;
				findPreSuc(root->right,pre,suc,key);
			}
		}
		void driver(){
			int key = 65;    //Key to be searched in BST
		    Node *root = NULL;
		    root = insertNode(root, 50);
		    insertNode(root, 30);
		    insertNode(root, 20);
		    insertNode(root, 40);
		    insertNode(root, 70);
		    insertNode(root, 60);
		    insertNode(root, 80);
		    Node* pre = NULL, *suc = NULL;
		    findPreSuc(root, pre, suc, key);
		    if (pre != NULL)
		      cout << "Predecessor is " << pre->data << endl;
		    else
		      cout << "No Predecessor";
		 
		    if (suc != NULL)
		      cout << "Successor is " << suc->data;
		    else
		      cout << "No Successor";
		}
};
int main(){
	BinSTree bst;
	bst.driver();
}
