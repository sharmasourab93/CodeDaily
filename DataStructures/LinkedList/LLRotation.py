class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

def push(node,data):
    if node is None:
        return Node(data)
    temp=Node(data)
    temp.next=node
    node=temp
    return node

def printLL(node):
    temp=node
    while temp is not None:
        print(temp.data,end="->")
        temp=temp.next
def pop(node):
    temp=node.next
    t1=node
    t1.next=None
    node=temp

    return [t1,node]


def rotation(node,k):
    temp=node
    t1=node
    for i in range(k):
        p_node,temp=pop(node)
        while temp.next is not None:
            temp=temp.next
        temp.next=p_node
"""def rotation(node,k):
    temp=node
    t1=None
    t2=t1
    while k>0 and temp is not None:
        t1.next=temp
        temp=temp.next
        k-=1
    t1.next=None
    kthnode=temp
    while temp is not None:
        temp=temp.next
    temp.next=t2
    while t2 is not None:
        temp=temp.next
        temp.next=t2.next
    return node"""

N=Node(1)
N=push(N,2)
N=push(N,3)
N=push(N,4)
N=push(N,5)

printLL(N)
N=rotation(N,2)
print("\nLinked List After Rotation")
printLL(N)