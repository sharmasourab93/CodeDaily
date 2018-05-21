class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
def findnode(root,data):
    if root==None:
        return False
    if root.data==data:
        return True
    if(findnode(root.left,data) or findnode(root.right,data)):
        print(root.data)
        return True
    return False
root=Node(1)
root.left=Node(2)
root.right=Node(3)
root.left.left=Node(4)
root.left.right=Node(5)
root.left.left.left=Node(7)
findnode(root,7)
            
