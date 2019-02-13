"""
Python: Binary Search Tree (BST)
"""


# BST Structure
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key


# In Order Traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)


# Insert Node in the tree
def insert(node, key):
    if node is None:
        return Node(key)

    if key < node.key:
        node.left = insert(node.left, key)

    else:
        node.right = insert(node.right, key)

    return node


# Returns the Minimum Value to the node
def min_value(node):
    current = node

    while current.left is not None:
        current = current.left

    return current


# For deleting a node and balance the BST
def delete_node(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete_node(root.left, key)

    elif key > root.key:
        root.right = delete_node(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = min_value(root.right)
        root.key = temp.key
        root.right = delete_node(root.right, temp.key)

    return root


# To Count K Min values
def count_k(self, node, k):
        s = []

        if node is not None and len(s) < k:
            self.count_k(node.left, k)
            s.append(node.data)
            self.count_k(node.right, k)

        print(s)


if __name__ == "__main__":
    root = None
    root = insert(root, 50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)

    print("In Order", end=" ")
    inorder(root)

    print("\nAfter deleting 20", end=":")
    root = delete_node(root, 20)

    inorder(root)

    print("\nAfter deleting 50", end=":")
    root = delete_node(root, 50)

    inorder(root)