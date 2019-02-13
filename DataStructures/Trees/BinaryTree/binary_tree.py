"""
Python : Binary Tree Data Structure
         Printing the Binary Tree in:
            1. Pre-order Traversal
            2. In-order Traversal
            3. Post-order Traversal
"""


# Node Structure for a Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


# Pre-order traversal of binary tree
def pre_order(root):

    print(root.data, end=" ")

    if root.left is not None:
        pre_order(root.left)

    if root.right is not None:
        pre_order(root.right)


# Post-order traversal of binary tree
def post_order(root):

    if root.left is not None:
        post_order(root.left)

    if root.right is not None:
        post_order(root.right)

    print(root.data, end=" ")


# In-order traversal of binary tree
def in_order(root):

    if root.left is not None:
        post_order(root.left)

    print(root.data, end=" ")

    if root.right is not None:
        post_order(root.right)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)

    print("Pre-order", end=":")
    pre_order(root)

    print("\nIn-order", end=":")
    in_order(root)

    print("\nPost-order", end=":")
    post_order(root)
