"""
Python: Binary Search Tree (BST)
        Delete an element from a BST
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


def min_value_node(root):
    current = root

    while current.left is not None:
        current = current.left

    return current


def delete_node(root, data):
    if root is None:
        return root

    if root.data > data:
        root.left = delete_node(root.left, data)

    elif root.data < data:
        root.right = delete_node(root.right, data)

    else:

        if root.left is None:
            temp, root = root.right, None
            return temp

        elif root.right is None:
            temp, root = root.left, None
            return temp

        temp = min_value_node(root.right)
        root.data = temp.data
        root.right = delete_node(root.right, temp.data)

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
    print("\n After delete")

    delete_node(root, 40)
    in_order(root)