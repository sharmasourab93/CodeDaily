"""
Python: Binary Tree
        Vertical Order Traversal
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Naive Vertical Order Traversal Approach
def find_min_max(root, minimum, maximum, hd):
    if root is None:
        return root

    if hd < minimum:
        minimum = hd
    elif hd > maximum:
        maximum = hd

    find_min_max(root.left, minimum, maximum, hd-1)
    find_min_max(root.right, minimum, maximum, hd+1)


def print_node_on_level(root, line, hd):
    if root is None:
        return root

    if hd == line:
        print(root.data, end=" ")

    print_node_on_level(root.left, line, hd-1)
    print_node_on_level(root.right, line, hd+1)


def vertical_order_traversal(root):
    mini, maxi = 0, 0

    find_min_max(root, mini, maxi, 0)

    for i in range(mini, maxi+1):
        print_node_on_level(root, i, 0)


# Optimized/Dictionary based approach
def get_vertical_order_optimized(root, hd, hash_map):
    if root is None:
        return

    hash_map[hd] = root.data

    get_vertical_order_optimized(root.left, hd-1, hash_map)
    get_vertical_order_optimized(root.right, hd+1, hash_map)


# TODO Fixing optimized vertical order traversal
def optimized_vertical_traversal(root):
    if root is None:
        return root

    hash_map = dict()

    get_vertical_order_optimized(root, 0, hash_map)

    for k, v in hash_map.items():
        print(k, v)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.left = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(8)

    print("Naive Vertical Order Traversal")
    vertical_order_traversal(root)
    print("\nOptimized Vertical Order Traversal")
    optimized_vertical_traversal(root)