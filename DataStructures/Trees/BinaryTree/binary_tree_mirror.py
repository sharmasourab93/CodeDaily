"""
Python: Binary Tree
        Convert a given binary tree to its mirror
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def mirror(root):
    if root is None:
        return

    mirror(root.left)
    mirror(root.right)

    root.left, root.right = root.right, root.left


def in_order(root):

    if root is None:
        return

    in_order(root.left)
    print(root.data, end=" ")
    in_order(root.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(7)
    print("Original tree")
    in_order(root)
    print("\nAfter Mirror")
    mirror(root)
    in_order(root)
