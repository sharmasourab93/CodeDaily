#include<iostream>
using namespace std;
class BinTree{
	public:
		struct Node{
			int data;
			Node *left, *right;
		};
		Node * newNode(int data){
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
		int *extractKeys(int in[], int l[], int m, int n){
			int *newlevel=new int[m],j=0;
			for(int i=0;i<n;i++){
				if(search(in,0,m-1,l[i])!=-1){
					newlevel[j]=l[i],j++;
				}
			}
			return newlevel;
		}
		// From Given In & Level Order Build tree
		Node *buildTree(char in[],char l[],int begin,int end,int n){
			static int preIndex=0;
			
			if(begin>end) return NULL;
			
			Node *tNode=newNode(l[preIndex++]);
			
			if(begin==end) return tNode;
			
			int inIndex=search(in,begin,end,tNode->data);
			
			int *llevel=extractKeys(in,l,inIndex,n);
			int *rlevel=extractKeys(in+inIndex+1,l,n-inIndex-1,n);
			
			tNode->left=buildTree(in,llevel,begin,inIndex-1,n);
			tNode->right=buildTree(in,rlevel,inIndex+1,end,n);
			
			delete []llevel;
			delete []rlevel;
			
			return tNode;
		}
		void printTree(Node *root){
			if(root==NULL) return;
			printTree(root->left);
			cout<<root->data<<" ";
			printTree(root->right);
		}
		void driver(){
			int in[]={4,8,10,12,14,20,22};
			int l[]={20,8,22,4,12,10,14};
			int len=sizeof(in)/sizeof(in[0]);
			Node *root=buildTree(in,l,0,len-1,len);
			printTree(root);
		}
};
int main(){
	BinTree bt;
	bt.driver();
}
