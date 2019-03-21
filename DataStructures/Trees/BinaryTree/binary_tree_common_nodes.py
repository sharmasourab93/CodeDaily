"""
Python: Binary Tree
The following program has below objectives
   i.Finding Ancestors of a single node
  ii.Finding Lowest Common Ancestor
 iii.Finding all the common nodes
"""


# Binary Tree Node Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def print_ancestors(root, key):
    """
       For a specified key value,
       prints all the predecessors
       leading up to the root
    """

    if root is None:
        return False

    if root.data == key:
        print(root.data)
        return True

    if print_ancestors(root.left, key) or \
            print_ancestors(root.right, key):
        print(root.data, end=" ")
        return True

    return False


def lowest_common_ancestor(root, key1, key2):
    """
        Prints the common predecessor nodes
        between two distinct nodes.
    """

    if root is None:
        return None

    if root.data == key1 or root.data == key2:
        return root

    left = lowest_common_ancestor(root.left, key1, key2)
    right = lowest_common_ancestor(root.right, key1, key2)

    if left and right:
        return root

    if left is None:
        return right
    else:
        return left


def find_common_nodes(root, first, second):
    """
    Finding all the parent nodes
    between first and second nodes.
    """
    lca = lowest_common_ancestor(root, first, second)

    if lca is None:
        return False

    print_ancestors(root, lca.data)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.left = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(8)

    # To Print all the ancestors of a node
    value = 6
    print("Printing Ancestors for ", end=" ")
    print_ancestors(root, value)

    # To Find the Lowest common Ancestor
    first, second = 4, 5
    print("\nLowest common Ancestor", end=": ")
    find_common_nodes(root, first, second)