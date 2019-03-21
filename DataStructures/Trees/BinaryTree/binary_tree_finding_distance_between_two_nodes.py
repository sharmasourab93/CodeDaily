"""
Python: Binary Tree
        Finding Distance between two nodes
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Method 1
def path_to_node(root, path, k):

    if root is None:
        return False

    path.append(root.data)

    if root.data == k:
        return True

    if ((root.left and path_to_node(root.left, path, k)) or
       (root.right and path_to_node(root.right, path, k))):
        return True

    path.pop()

    return False


def distance_in_nodes(root, first, second):
    if root:
        path1 = []
        path_to_node(root, path1, first)

        path2 = []
        path_to_node(root, path2, second)

        i = 0
        while i < len(path1) and i < len(path2):

            if path1[i] != path2[i]:
                break

            i += 1

        return (path1.__len__() +
                path2.__len__() -
                2 * i
                )

    else:
        return 0


# Method 2
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


def find_level(root, data, d, level):
    if root is None:
        return

    if root.data == data:
        d.append(level)
        return

    find_level(root.left, data, d, level + 1)
    find_level(root.right, data, d, level + 1)


def find_distance(root, first, second):
    lca = lowest_common_ancestor(root, first, second)

    d1, d2 = [], []

    if lca:
        find_level(lca, first, d1, 0)
        find_level(lca, second, d2, 0)
        return d1[0] + d2[0]

    else:
        return -1


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.left = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.right.left.left = Node(8)
    # root.left.left.left = Node(9)

    f, s = 5, 7

    # Method 1
    distance1 = distance_in_nodes(root, f, s)
    print("Distance between {} and {} is {}".format(f, s, distance1))
    # Method 2
    distance2 = find_distance(root, f, s)
    print("Distance between {} and {} is {} using LCA method"
          .format(f, s, distance2))