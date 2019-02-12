"""
Python : Binary Tree Data Structure
"""


# Node Structure for a Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


# To Print Binary Tree Node Values
def print_tree(root):
    print(root.data)

    if root.left is not None:
        print_tree(root.left)

    if root.right is not None:
        print_tree(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
print_tree(root)
