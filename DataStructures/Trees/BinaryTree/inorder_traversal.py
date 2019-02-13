"""
Python: In-Order Traversal Without Recursion in a Binary Tree
"""


# Binary Tree Structure
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


def in_order(root):
    # Set current to root of Binary tree
    current = root
    s = []
    done = 0

    while not done:

        if current is not None:
            # Place pointer to a tree node on the stack before
            # traversing the node's left subtree
            s.append(current)
            current = current.left

        else:
            if len(s) > 0:
                current = s.pop()
                print(current.data)
                current = current.right

            else:
                done = 1


if __name__ == "__main__":
    root_node = Node(1)
    root_node.left = Node(2)
    root_node.right = Node(3)
    root_node.left.left = Node(4)
    root_node.left.right = Node(5)

    in_order(root_node)
