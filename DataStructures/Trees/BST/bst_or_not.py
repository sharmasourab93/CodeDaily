"""
Python: Binary Search Tree(BST)
        Is the given tree Bst or not?
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


prev = None


def is_bst(root):

    global prev

    if root is None:
        return True

    if root:
        if not is_bst(root.left):
            return False

        if prev is not None and root.data <= prev.data:

            return False

        prev = root

        return is_bst(root.right)


if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(1)
    root.left.right = Node(3)

    print("In Order", end=" ")
    in_order(root)

    print("\nIs BST?", end=" ")
    if is_bst(root) is True:
        print("Yes.")
    else:
        print("No.")