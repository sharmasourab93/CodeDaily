class Node:
    
    def __init__(self, data):
        self.data = data
        self.left = self.right = None
        

def inorder(root):
    if root is None:
        return
    
    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


def height(root):
    
    if root is None:
        return 0
    
    left = 1 + height(root.left)
    right = 1 + height(root.right)
    
    return max(left, right)


def level_util(root, level):
    
    if root is None:
        return
    
    if level == 1:
        print("Printing Data", root.data, end=" ")
        
    elif level > 1:
        level_util(root.left, level-1)
        level_util(root.right, level-1)
        

def level_traversal(root):
    h = height(root)
    for i in range(1, h+1):
        print("Level ", i, end=" ")
        level_util(root, i)
        print("")


def vertical_traversal_util(root, level, mapd):
    if root is None:
        return
    
    mapd[level].append(root.data)
    
    vertical_traversal_util(root.left, level-1, mapd)
    vertical_traversal_util(root.right, level+1, mapd)


def vertical_traversal(root):
    h = height(root)
    mapd = dict()
    for i in range(-h + 1, h - 1):
        mapd[i] = []
    
    vertical_traversal_util(root, 0, mapd)
    result = []
    range_ = list(mapd.keys())
    for i in range_:
        if len(mapd[i]) != 0:
            result.append(mapd[i].pop(0))
            
    return result
    
    
if __name__ == '__main__':
    root = Node(1)
    root.right = Node(2)
    root.right.right = Node(5)
    root.right.right.right = Node(6)
    root.right.right.left = Node(3)
    root.right.right.left.right = Node(4)
    
    result = vertical_traversal(root)
    print(' '.join(list(map(str, result))))
