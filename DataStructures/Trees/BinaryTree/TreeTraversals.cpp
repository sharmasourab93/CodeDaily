//Implementation of Tree Traversals 
#include<iostream>
using namespace std;
struct Node{
	int data;
	Node *left;
	Node *right;
};

Node *newNode(int data){
	Node *temp=new Node();
	temp->data=data;
	temp->left=temp->right=NULL;
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

//Inorder Traversal Left Root Right
void InOrder(Node *root){
	if(root==NULL)return;
	InOrder(root->left);
	cout<<root->data<<" ";
	InOrder(root->right);
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

//Preorder Traversal Root Left Right
void PreOrder(Node *root){
	if(root==NULL)return ;
	cout<<" "<<root->data;
	PreOrder(root->left);
	PreOrder(root->right);
}	

//Post Order Traversal Left Right Root
void PostOrder(Node *root){
	if(root==NULL)return;
	PostOrder(root->left);
	PostOrder(root->right);
	cout<<" "<<root->data;
}

//Level Order Traversal
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

//Vertical Order Traversal
//Start of Hashmap Based Optimized solution
void getVerticalOrder(Node *root,int hd,map<int,vector<int> > &m){
	if(root==NULL) return;

	m[hd].push_back(root->data);

	getVerticalOrder(root->left,hd-1,m);
	getVerticalOrder(root->right,hd+1,m);
}

void printVerticalOrder(Node *root){
	if (root==NULL) return;
	map<int,vector<int> > v;
	getVerticalOrder(root,0,v);

	map<int,vector<int> >::iterator i;

	for(i=v.begin();i!=v.end();i++){
		for(int j=0;j<i->second.size();++j){
			cout<<i->second[j]<<" ";
		}
		cout<<endl;
	}

}
//End of Hashmap Based Optimized Solution

// Start of Naive Solution
void findMinMax(Node *root,int *min,int *max,int hd){
	if (root==NULL) return;
	if(hd<*min){ *min=hd;}
	else if(hd>*max){*max=hd;}

	findMinMax(root->left,min,max,hd-1);
	findMinMax(root->right,min,max,hd+1);
}

void printLine(Node *root,int line_no,int hd){
	if (root==NULL) return;

	if(hd==line_no){ cout<<root->data<<" ";}

	printLine(root->left,line_no,hd-1);
	printLine(root->right,line_no,hd+1);

}

void verticalOrder(Node *root){
	int min=0,max=0;
	findMinMax(root,&min,&max,0);

	for(int line_no=min;line_no<=max;line_no++){
		printLine(root,line_no,0);
		cout<<endl;
	}
}

int main(){
	Node *root = newNode(1);
    root->left = newNode(2);
    root->right = newNode(3);
    root->left->left = newNode(4);
    root->left->right = newNode(5);
    root->right->left = newNode(6);
    root->right->right = newNode(7);
    root->right->left->right = newNode(8);
    root->right->right->right = newNode(9);

    cout<<"Inorder Traversal:"<<endl;
    InOrder(root);
    cout<<"\nPreorder Traversal:"<<endl;
    PreOrder(root);
    cout<<"\nPostorder Traversal:"<<endl;
    PostOrder(root);
    cout<<endl;
}
