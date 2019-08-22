"""
Python: Binary Search Tree (BST)
        Find Lowest Common Ancestor
"""


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def in_order(root):
    if root is None:
        return

    in_order(root.left)
    print(root.data, end=" ")
    in_order(root.right)


def insert_node(root, data):
    if root is None:
        root = Node(data)

    if root.data > data:
        root.left = insert_node(root.left, data)

    elif root.data < data:
        root.right = insert_node(root.right, data)

    return root


def lca(root, n1, n2):

    if root is None:
        return None

    if root.data > n1 and root.data > n2:
        return lca(root.left, n1, n2)

    if root.data < n1 and root.data < n2:
        return lca(root.right, n1, n2)

    return root


if __name__ == '__main__':
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    n1, n2 = 10, 14
    result = lca(root, n1, n2)
    print("Lowest Common Ancestor for {} and {} is {}".format(n1, n2, result.data))

    n1, n2 = 4, 22
    result = lca(root, n1, n2)
    print("Lowest Common Ancestor for {} and {} is {}".format(n1, n2, result.data))