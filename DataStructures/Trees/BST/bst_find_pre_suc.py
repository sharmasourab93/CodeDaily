"""
Python: Binary Search Tree (BST)
        Find Inorder Predecessor & Successor
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


def find_pre_suc(root, key):
    if root is None:
        return

    if root.data == key:

        if root.left is not None:
            temp = root.left
            while temp.right:
                temp = temp.right

            find_pre_suc.pre = temp

        if root.right is not None:
            temp = root.right
            while temp.left:
                temp = temp.left

            find_pre_suc.suc = temp

        return

    if root.data > key:
        find_pre_suc.suc = root
        find_pre_suc(root.left, key)

    else:
        find_pre_suc.pre = root
        find_pre_suc(root.right, key)


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
    key = 60
    find_pre_suc.pre = None
    find_pre_suc.suc = None
    find_pre_suc(root, key)

    if find_pre_suc.pre is not None:
        print("Predecessor is", find_pre_suc.pre.data)
    else:
        print("No Predecessor")

    if find_pre_suc.suc is not None:
        print("Successor is", find_pre_suc.suc.data)
    else:
        print("No Successor")