#include<iostream>
#include<queue>
using namespace std;

struct Node{
	int data;
	Node * left,*right;
};

Node *newNode(int data){
	Node * temp=new Node();
	temp->data=data;
	temp->left=NULL;
	temp->right=NULL;

	return temp;
}
int max(int a, int b){
	return a>b?a:b;
}
int height(Node *root){
	if(root==NULL){
		return 0;
	}
	int l=1+height(root->left);
	int r=1+height(root->right);
	int m=max(l,r);
	return m;
}

// O(n^2) Complexity
//Also considers Height
void LevelOrderTraversalUtil(Node *root,int level){
	if (root==NULL) return;
	if (level==1) cout<<root->data<<" ";
	else if(level>1){
		LevelOrderTraversalUtil(root->left,level-1);
		LevelOrderTraversalUtil(root->right,level-1);
	}
}
void LevelOrderTraversal(Node *root){
	if(root!=NULL){
		int h=height(root);
		for(int i=1;i<=h;i++){
			LevelOrderTraversalUtil(root,i);
			cout<<endl;
		}
	}
}
//Takes O(n) Complexity
//Iterative Level Order Traversal
void ILevelOrderTraversal(Node *root){
	if (root==NULL) return;

	queue<Node *>q;

	q.push(root);

	while(1){
		int nodeCount=q.size();

		if(nodeCount==0) break;

		while(nodeCount>0){
			Node *node=q.front();
			cout<<node->data<<" ";
			q.pop();

			if(node->left!=NULL){
				q.push(node->left);
			}
			if(node->right!=NULL){
				q.push(node->right);
			}
			nodeCount--;
		}
		cout<<endl;
	}
}


int main(){

	Node *root=newNode(1);
	root->left=newNode(2);
	root->right=newNode(3);
	root->left->left=newNode(4);
	root->left->right=newNode(5);
	root->right->left=newNode(6);
	root->right->right=newNode(7);
	cout<<"Level Order Traversal O(n^2)"<<endl;
	LevelOrderTraversal(root);
	cout<<endl<<"Iterative Level Order Traversal O(n)"<<endl;
	ILevelOrderTraversal(root);

}