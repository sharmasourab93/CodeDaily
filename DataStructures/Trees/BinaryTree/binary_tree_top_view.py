class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        

def inorder(root):
    if root is None:
        return
    
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)
