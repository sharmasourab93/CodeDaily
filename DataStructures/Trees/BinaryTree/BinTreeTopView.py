class Node:
    def __init__(self,data=None,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
def newNode(self,data):
    return Node(data)

def printTree(self,root):
    if root is None: return None
    printTree(root.left)
    print(root.data)
    printTree(root.right)

def topView(self,root):
    if root is None:
        return
    queue={}
    u_map={}

    while queue:

