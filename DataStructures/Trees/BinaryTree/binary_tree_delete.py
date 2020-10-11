"""
Python: Binary Tree
        Deleting a Node in the Binary Tree & Replacing
"""


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


def in_order(root):
    if root is not None:
        in_order(root.left)
        print(root.data, end=" ")
        in_order(root.right)


def delete_deepest(root, item):
    
    queue = list()
    queue.append(root)
    
    temp = None
    
    while len(queue) != 0:
        
        temp = queue.pop()
        if temp == item:
            temp = None
            del item
            return
        
        if temp.right:
            if temp.right == item:
                temp.right = None
                del item
                return
            else:
                queue.append(temp.right)
                
        if temp.left:
            if temp.left == item:
                temp.left = None
                del item
                return
            else:
                queue.append(temp.left)


def delete_node(root, key):
    
    if root is None:
        return root
    
    if root.left is None and root.right is None:
        return root if root.data == key else None
    
    queue = list()
    queue.append(root)
    key_node = item = None
    
    while len(queue) != 0:
        
        item = queue.pop(0)
        
        if item.data == key:
            key_node = item
            
        if item.left:
            queue.append(item.left)
            
        if item.right:
            queue.append(item.right)
            
    if key_node is not None:
        x = item.data
        delete_deepest(root, item)
        key_node.data = x
    
    return root
        

if __name__ == "__main__":
    root = Node(13)
    root.left = Node(12)
    root.right = Node(10)
    root.left.left = Node(4)
    root.left.right = Node(19)
    root.right.right = Node(9)
    root.right.left = Node(16)
    
    print("Printing Nodes Inorder", end=":")
    in_order(root)
    
    value = 12
    print("\nPrinting nodes after deletion of value {0}:"
          .format(value), end=" ")
    root = delete_node(root, value)
    in_order(root)
