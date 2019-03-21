"""
Python: Binary Tree
The following program does as below
   i. Finding Height of the Binary Tree
  ii. Finding Diameter/Distance of the Binary Tree
"""


# Binary Tree Node Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def height(root):
    """To find the height of binary tree"""
    if root is None:
        return 0

    left = 1 + height(root.left)
    right = 1 + height(root.right)

    return max(left, right)


def diameter(root):
    """To find the diameter of a binary tree"""
    if root is None:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    left_diameter = diameter(root.left)
    right_diameter = diameter(root.right)

    return max(left_height + right_height + 1,
               max(left_diameter, right_diameter)
               )


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.left = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(8)
    # root.left.left.left = Node(9)

    # To Print the height of a binary tree
    h = height(root)
    print("Height of a binary Tree", h)

    # To print the diameter of a binary tree
    d = diameter(root)
    print("Diameter of a binary tree", d)

