class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key
def printTree(root):
    print(root.data)
    if(root.left!=None):
        #print(root.left.data)
        printTree(root.left)
    if(root.right!=None):
        #print(root.right.data)
        printTree(root.right)
    return
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
printTree(root)
