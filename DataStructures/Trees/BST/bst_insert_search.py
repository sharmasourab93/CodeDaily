"""
Python: Binary Search Tree (BST)
        Insert an element in a BST
        Search an element in a BST
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


def search(root, key):
    if root is None:
        return False

    if root.data == key:

        return True

    if root.data > key:
        return search(root.left, key)

    else:
        return search(root.right, key)


def insert_node(root, data):
    if root is None:
        root = Node(data)

    if root.data > data:
        root.left = insert_node(root.left, data)

    elif root.data < data:
        root.right = insert_node(root.right, data)

    return root


if __name__ == "__main__":
    root = None
    root = insert_node(root, 50)
    root = insert_node(root, 30)
    root = insert_node(root, 20)
    root = insert_node(root, 40)
    root = insert_node(root, 70)
    root = insert_node(root, 60)
    root = insert_node(root, 80)

    print("In Order", end=" ")
    in_order(root)
    print()

    find = 80
    find_element = search(root, find)

    if find_element:
        print("{} found.".format(find))

    else:
        print("{} not found".format(find))
