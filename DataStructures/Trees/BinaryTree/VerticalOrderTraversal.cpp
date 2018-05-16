#include<iostream>
#include<vector>
#include<map>
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
// End of Naive Solution
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

	cout<<"Naive Vertical Order:"<<endl;
	//O(w*n) w=width, n= nodes in BT
	//O(N^2)
	verticalOrder(root);

	cout<<"\nOptimized Hashmap Based Vertical Ordering: "<<endl;
	//O(n Log n) solution 
	//O(n) for insertion and log n for map operation
	printVerticalOrder(root);
}

