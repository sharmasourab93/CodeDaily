class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


# In Order Traversal of BST
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
    
    return root


def insert(root, data):
    if root is None:
        return Node(data)
    
    if data < root.data:
        root.left = insert(root.left, data)
    
    if data > root.data:
        root.right = insert(root.right, data)
    
    return root


def kth_largest(root, k, c):
    if root is None or c[0] >= k:
        return

    kth_largest(root.right, k, c)
    c[0] += 1
    
    if c[0] == k:
        print(root.data)
        return

    kth_largest(root.left, k, c)
    

def kth_smallest(root, k, c=None):
    
    if c is None:
        c = [0]
    
    if root is None or c[0] >= k:
        return
    
    kth_smallest(root.left, k, c)
    
    c[0] += 1
    
    if c[0] == k:
        print(root.data)
        return
    
    kth_smallest(root.right, k, c)
    


if __name__ == '__main__':
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
    
    k, list_ = 3, [0]
    print("\n {0} largest".format(k))
    kth_largest(root, k, list_)
    
    print("\n{0} smallest".format(k))
    kth_smallest(root, k)
