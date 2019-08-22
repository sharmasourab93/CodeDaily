"""
Python: Binary Tree Traversal
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

def inorder(root):
    if root.left is not None:
        inorder(root.left)

    print(root.data)

    if root.right is not None:
        inorder(root.right)


def level_order_util(root, level):

    if root is None:
        return

    if level == 1:
        print(root.data, end=" ")

    else:
        level_order_util(root.left, level-1)
        level_order_util(root.right, level -1)


def level_order_traversal(root):
    if root is None:
        return

    h = height(root)

    for i in range(1, h+1):
        level_order_util(root, i)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.left = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(8)

    level_order_traversal(root)