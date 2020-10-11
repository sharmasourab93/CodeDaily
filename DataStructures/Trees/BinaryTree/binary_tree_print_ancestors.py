"""
Python: Binary Tree
        Print Ancestors of the Binary Tree
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def print_ancestors(root, data):
    if root is None:
        return False

    if root.data == data:
        return True

    if print_ancestors(root.left, data) or \
            print_ancestors(root.right, data):
        print(root.data)
        return True

    return False


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.left.left.left = Node(7)

    print_ancestors(root, 4)
