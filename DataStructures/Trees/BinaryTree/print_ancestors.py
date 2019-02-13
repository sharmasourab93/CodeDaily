"""
Python : Finding Ancestors of a node in Binary Tree
"""


# Node Structure for a Binary Tree
class Node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data


# Finding the Ancestor Node
def find_node(root, data):
    if root is None:
        return False

    if root.data == data:
        return True

    if find_node(root.left, data) or find_node(root.right, data):
        print(root.data)
        return True

    return False


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(7)

    print(find_node(root, 7))