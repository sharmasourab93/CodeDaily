Node *insertNode(Node *root,int data){
	if root==NULL return newNode(data);
	if data<root->data root->left=insertNode(root->left,data);
	if data>root->data root->right=insertNode(root->right,data);
}

Node *deleteNode(Node *root,int data){
	if root==NULL return root
	if data<root->data{
		root->left=deleteNode(root->left,data);
	}
	else if data>root->data{
		root->right=deleteNode(root->right,data)
	}
	else{
		if node->left == NULL{
			Node *temp=node->right;
			free(node);
			return temp;
		}
		else if node->right==NULL
			Node *temp=node->left;
			free(node);
			return temp;
		Node *temp=minValueNode(node->right)
		node->data=temp->data
		node->right=delteNode(node->right,temp->data)
		return node
	}
}

Node *lca(Node *root,int d1,int d2){
	if root==NULL: return root
	
	if root->data>n1 && root->data>n2: return lca(root->left,n1,n2)
	if root->data<n1 && root->data<n2: return lca(root->right,n1,n2)
}



bool isbstornot(Node *root,int min,int max){
	return isbstornot(root,min,max)
}
