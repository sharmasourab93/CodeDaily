"""
Python: Binary Search Tree (BST)
"""


class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.key=key
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)
def insert(node, key):
    if node is None:
        return Node(key)
    if key<node.key:
        node.left=insert(node.left,key)
    else:
        node.right=insert(node.right,key)
    return node
def minValueNode(node):
    current=node
    while(current.left is not None):
        current=current.left
    return current
def DeleteNode(root,key):
    if root is None:
        return root
    if key<root.key:
        root.left=DeleteNode(root.left,key)
    elif(key>root.key):
        root.right=DeleteNode(root.right,key)
    else:
        if root.left is None:
            temp=root.right
            root=None
            return temp
        elif root.right is None:
            temp=root.left
            root=None
            return temp
        temp=minValueNode(root.right)
        root.key=temp.key
        root.right=DeleteNode(root.right,temp.key)
    return root
root=None
root=insert(root,50)
root=insert(root,30)
root=insert(root,20)
root=insert(root,40)
root=insert(root,70)
root=insert(root,60)
root=insert(root,80)

print("Inorder")
inorder(root)
print("\nAfter deleting 20")
root=DeleteNode(root,20)
inorder(root)
print("\nAfter deleting 50")
root=DeleteNode(root,50)
inorder(root)
        
