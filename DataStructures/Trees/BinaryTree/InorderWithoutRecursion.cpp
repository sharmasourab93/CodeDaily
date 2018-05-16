#include<iostream>
#include<stack>
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

void InorderWithoutRecursion(Node *root){
	stack<Node *> S=new stack();
	Node *current=root;


	while(current!=NULL){
		S.push(current->left);
		current=current->left;
	}

	while(S.size()>0){
		current=S.top();
		cout<<current->data<<" ";
		S.pop();
		if(current->right!=NULL){
			current=current->right;
			while(current!=NULL){
				S.push(current->right);
				current=current->right;
			}
		}
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
	InorderWithoutRecursion(root);
}