"""
Python: In-order Predecessor & Successor in a Binary Tree
"""


# Binary Tree Structure
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# To Find Successor Predecessor
def find_pre_suc(root, key):
    if root is None:
        return root

    if root.key == key:
        if root.left is not None:
            tmp = root.left
            while tmp.right:
                tmp = tmp.right

            find_pre_suc.pre = tmp

        if root.right is not None:
            tmp = root.right
            while tmp.left:
                find_pre_suc.suc = tmp
        return root

    if root.key > key:
        find_pre_suc.suc = root
        find_pre_suc(root.left, key)

    else:
        find_pre_suc.pre = root
        find_pre_suc(root.right, key)


# To Insert Node into
def insert(node, key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)

    else:
        node.right=insert(node.right,key)

    return node


if __name__ == "__main__":
    key = 40

    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    find_pre_suc.pre = None
    find_pre_suc.suc = None
    find_pre_suc(root, key)

    if find_pre_suc.pre is not None:
        print("Predecessor is", find_pre_suc.pre.key)

    else:
        print("No predecessor")

        if find_pre_suc.suc is not None:
            print("Successor is", find_pre_suc.suc.key)

        else:
            print("No Sucessor")