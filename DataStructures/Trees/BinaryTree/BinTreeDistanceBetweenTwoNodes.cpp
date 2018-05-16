#include<iostream>
#include<math.h>
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
		
		int height(Node *root){
			if(root==NULL) return 0;
			int l=1+height(root->left);
			int r=1+height(root->right);
			return (l>r?l:r);
		}

		int findlevelUtil(Node *root,int data,int level){
			if(root==NULL) return -1;
			if(level==1 && root->data==data) return 0;
			int l=1+findlevelUtil(root->left,data,level-1);
			int r=1+findlevelUtil(root->right,data,level-1);

			return (l<r?l:r);
		}

		int findlevel(Node *root,int data,int h){
			for (int i=1;i<=h;i++){
				int l=findlevelUtil(root,data,i);
				return l;
			}
		}

		int distance(Node *root,int data1,int data2){
			int h=height(root);
			return(abs(findlevel(root,data1,h)+findlevel(root,data2,h)));
		}

		//Primary driver function 
		void driver(){
			Node * root=newNode(1);
			root->left=newNode(2);
			root->right=newNode(3);
			root->left->right=newNode(4);
			root->left->left=newNode(5);
			root->left->left->left=newNode(6);
			int dist=distance(root,4,3);
			cout<<dist<<endl;
			
		}
};
int main(){
	BinTree bt;
	bt.driver();
}
