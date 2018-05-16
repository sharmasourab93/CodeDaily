#include<iostream>
using namespace std;

class BinTree{
	public:
		struct Node{
			char data;
			Node *left, *right;
		};
		Node * newNode(char data){
			Node * temp=new Node();
			temp->data=data;
			temp->left=NULL;
			temp->right=NULL;
			return temp;
		}	
		//Search Index of the Node value
		int search(char arr[],int strt,int end,char value){
			for(int i=strt;i<=end;i++){
				if(arr[i]==value){
					return i;
				}
			}
		}
		//Build BinTree from given Inorder & Postorder 
		Node *buildTree(char in[],char pre[],int inStrt,int inEnd ){
			static int preIndex=0;
			
			if(inStrt>inEnd) return NULL;
			
			Node *tNode=newNode(pre[preIndex++]);
			
			if(inStrt==inEnd) return tNode;
			
			int inIndex=search(in,inStrt,inEnd,tNode->data);
			
			tNode->left=buildTree(in,pre,inStrt,inIndex-1);
			tNode->right=buildTree(in,pre,inIndex+1,inEnd);
			
			return tNode;
		}
		
		void printTree(Node *root){
			if(root==NULL) return;
			printTree(root->left);
			cout<<root->data<<" ";
			printTree(root->right);
		}
		
		void driver(){
			char in[]={'D','B','E','A','F','C'};
			char pre[]={'A','B','D','E','C','F'};
			int len=sizeof(in)/sizeof(in[0]);
			Node *root=buildTree(in,pre,0,len-1);
			printTree(root);
		}
};
int main(){
	BinTree bt;
	bt.driver();
}
