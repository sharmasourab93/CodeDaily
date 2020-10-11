"""
Python: Binary Tree
        Vertical Order Traversal
"""


class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


def height(root):
    
    if root is None:
        return 0
    
    left = 1 + height(root.left)
    right = 1 + height(root.right)
    
    return max(left, right)


def vertical_traversal_util(root, level, mapd):
    if root is None:
        return
    
    mapd[level].append(root.data)
    
    vertical_traversal_util(root.left, level-1, mapd)
    vertical_traversal_util(root.right, level+1, mapd)


def vertical_traversal(root):
    h = height(root)
    mapd = {i: [] for i in range(-h + 1, h + 1)}
    
    vertical_traversal_util(root, 0, mapd)
            
    return {k: v for k, v in mapd.items() if len(v) != 0}
    
    
if __name__ == '__main__':
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(5)
    root.right.right.right = Node(6)
    root.right.right.left = Node(3)
    root.right.right.left.right = Node(4)
    root.right.right.left.left = Node(7)
    root.right.right.left.right = Node(8)
    root.right.right.left.right.left = Node(9)
    root.right.right.left.right.right = Node(10)
    root.left = Node(11)
    root.left.left = Node(12)
    root.left.right = Node(12)
    root.left.left.right = Node(13)
    root.left.left.left = Node(14)
    
    result = vertical_traversal(root)
    
    for k, v in result.items():
        print("Level {0}: [{1}]"
              .format(k, ' '.join(list(map(str, v)))))
