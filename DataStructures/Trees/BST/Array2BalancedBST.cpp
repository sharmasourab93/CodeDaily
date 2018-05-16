//A Sorted Array to a Balanced BST
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
		void printInorder(Node *root){
			if(root!=NULL){	
				printInorder(root->left);
				cout<<root->data<<" ";
				printInorder(root->right);
			}
		}
		void printArray(int *array, int size){
			cout<<"\nArray elements are: ";
			for(int i=0;i<size;i++){
				cout<<array[i]<<" ";
			}
			cout<<endl;
		}
		void insertionSort(int a[],int n){
			int i,j,min;
			for(i=1;i<n;i++){
				min=a[i];
				j=i-1;
				while(j>=0&&a[j]>min){
					a[j+1]=a[j];
					j--;
				}
				a[j+1]=min;
			}
			printArray(a,n);
		}
		//Sorted Array to a Balanced Binary Search tree
		Node *Sorted2BST(int array[],int low, int size){
			if(size<low) return NULL;
			int mid=(size+low)/2;
			Node * root=new Node();
			root=newNode(array[mid]);
			root->left=Sorted2BST(array,low,mid-1);
			root->right=Sorted2BST(array,mid+1,size);
			return root;
		}
		void driver(){
			int array[]={9,8,7,6,5,4,3,2,1};
			int size=((sizeof(array))/(sizeof(array[0])));
			insertionSort(array,size);
			//printArray(array,size);
			Node *root=NULL;
			root=Sorted2BST(array,0,size-1);
			printInorder(root);
		}
};
int main(){
	BinSTree bst;
	bst.driver();
}
