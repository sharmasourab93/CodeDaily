class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinMinTree:
    def insert(self,root,data):
        if root is None:
            return Node(data)
        if data<root.data:
            root.left=self.insert(root.left,data)
        elif data>root.data:
            root.right=self.insert(root.right,data)
        return root
    def inorder(self,root):
        if root is not None:
            self.inorder(root.left)
            print(root.data)
            self.inorder(root.right)
    def countK(self,root,k):
        s=[]
        l=0
        if root is not None and len(s)<k:
            self.countK(root.left,k)
            s.append(root.data)
            self.countK(root.right,k)
        print(len(s))
        print(s)
        #return s[]
    def driver(self):
        self.root=None
        self.root=self.insert(self.root,50)
        self.root=self.insert(self.root,30)
        self.root=self.insert(self.root,20)
        self.root=self.insert(self.root,40)
        self.root=self.insert(self.root,70)
        self.root=self.insert(self.root,60)
        self.root=self.insert(self.root,80)
        k=6
        print("\nInorder")
        self.inorder(self.root)
        zebra=self.countK(self.root,k)
        print(zebra)
        print("\nThe"+ str(k) +"th smallest element in the BST is: "+ str(zebra))
        
x=BinMinTree()
x.driver()
