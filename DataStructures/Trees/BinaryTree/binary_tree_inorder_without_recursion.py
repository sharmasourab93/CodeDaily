"""
Python: Binary Tree
        Inorder Traversal without recursion
"""


# Node Structure for a Binary Tree
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


# In-order Traversal with recursion
def in_order(root):

    if root.left is not None:
        in_order(root.left)

    print(root.data, end=" ")

    if root.right is not None:
        in_order(root.right)


# In-order Traversal without recursion
def in_order_without_recursion(root):
    stack = []
    current = root
    done = 0

    while not done:
        if current is not None:
            stack.append(current)
            current = current.left

        else:
            if len(stack) > 0:
                current = stack.pop()
                print(current.data, end=" ")
                current = current.right

            else:
                done = 1


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
    print("In-order traversal by recursion")
    in_order(root)
    print("\nIn-order traversal by iteration")
    in_order_without_recursion(root)