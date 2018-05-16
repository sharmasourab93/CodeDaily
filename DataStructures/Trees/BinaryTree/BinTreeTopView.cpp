//Top view of a tree
#include<iostream>
#include<map>
#include<queue>
#include<stdlib.h>
using namespace std;
struct Node {
	int data;
	Node *left,*right;
};
void topView(Node *root){
	if(root==NULL){
		return;
	}
	unordered_map<int,int>m;
	queue<pair<Node*,int>>q;
	//Push Node and Horizantal Distance to queue
	q.push(make_pair(root,0));
	while(!q.empty()){
		pair<Node *,int> p=q.front();
		Node *n=p.first;
		int val=p.second;
		q.pop();
		
		//If horizantal value is not in the hashmap
		//That means it is the frist value with athat 
		//horizontal distance so print it and store
		//this value in hashmap
		
		if(m.find(val)==m.end()){
			m[val]=n->data;
			cout<<n->data<<" ";
		}
		if(n->left!=NULL){
			q.push(make_pair(n->left,val-1));
		}
		if(n->right!=NULL){
			q.push(make_pair(n->right,val+1));
		}
	}
}
Node *newNode(int key){
	Node *node=new Node;
	node->data=key;
	node->left=node->right=NULL;
	return node;
}
int main(){
	Node *root=newNode(1);
	root->left=newNode(2);
	root->right=newNode(3);
	root->left->right=newNode(4);
	root->left->right->right=newNode(5);
	root->left->right->right->right=newNode(6);
	
	topView(root);
}
