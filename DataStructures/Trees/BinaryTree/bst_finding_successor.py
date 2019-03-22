"""
Python: Binary Tree
    i.  Finding Successor
   ii.  Finding Predecessor
"""


# Binary Tree Structure
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# To Insert Node into
def insert(node, key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)

    else:
        node.right = insert(node.right, key)

    return node


# Function to find the
# In-order predecessor & successor
def find_pre_suc(root, key):
    # Step 1: Base base
    if root is None:
        return root

    # Step 2: On Key matching root
    if root.key == key:
        # Iterate on left
        if root.left is not None:
            tmp = root.left
            while tmp.right:
                tmp = tmp.right

            find_pre_suc.pre = tmp

        # Iterate on right
        if root.right is not None:
            tmp = root.right
            while tmp.left:
                find_pre_suc.suc = tmp

        return root

    # 3. Redirect on bst properties
    if root.key > key:
        find_pre_suc.suc = root
        find_pre_suc(root.left, key)

    else:
        find_pre_suc.pre = root
        find_pre_suc(root.right, key)


if __name__ == "__main__":
    root = None
    root = insert(root, 50)
    insert(root, 30)
    insert(root, 20)
    insert(root, 40)
    insert(root, 70)
    insert(root, 60)
    insert(root, 80)

    key = 30
    find_pre_suc.pre = None
    find_pre_suc.suc = None
    find_pre_suc(root, key)


    if find_pre_suc.pre and find_pre_suc.suc:
        print("Predecessor is", find_pre_suc.pre.key,
              " Successor is", find_pre_suc.suc.key)

    # TODO: Fix the broken case here