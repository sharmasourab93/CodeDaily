"""
Python: Diameter of a binary tree
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    if root is None:
        return 0

    left = 1 + height(root.left)
    right = 1 + height(root.right)

    return max(left, right)


def diameter(root):

    if root is None:
        return 0

    lheight = height(root.left)
    rheight = height(root.right)

    ldiameter = diameter(root.left)
    rdiameter = diameter(root.right)

    return max(lheight + rheight + 1,
               max(ldiameter, rdiameter)
               )