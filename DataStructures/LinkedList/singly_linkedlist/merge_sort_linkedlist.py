"""
Python: Singly Linked List
        Merge Sort on Singly Linked List
"""


class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


def print_nodes(head):
    temp = head
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print("\n")
    

def get_middle(node1):
    if node1 is None:
        return None
    
    temp = node1
    slow, fast = temp, temp
    prev = None
    
    while fast.next and fast.next.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
        
    if prev is None:
        return None
    else:
        return prev.next
    

def merge(left, right):
    head = temp = None
    
    while left is not None and right is not None:
        if left.data < right.data:
            if head is None:
                head = left
                temp = head
                left = left.next
            else:
                temp.next = left
                left = left.next
            
        else:
            if head is None:
                head = right
                temp = head
                right = right.next
            else:
                temp.next = right
                right = right.next
        
        temp = temp.next
        
        
    while left is not None and right is None:
        temp.next = left
        temp = temp.next
        left = left.next
        print("left", temp.data)
        
    while right is not None and left is None:
        print("right is not None")
        temp.next = right
        temp = temp.next
        right = right.next
    
    return head
 
    
#TODO: Fixing Merge Sort for my own approach
def merge_sort(node1):
    # Base case
    if not node1:
        return node1
    
    temp = node1
    print_nodes(temp)
    prev_mid = get_middle(node1)
    partition = prev_mid
    
    while temp and temp.next != prev_mid:
        temp = temp.next
        
    temp = None
    
    print_nodes(temp)
    print_nodes(partition)
    
    # left = merge_sort(temp)
    # right = merge_sort(partition)
    
    #sorted_list = merge(left, right)
    
    # return sorted_list


if __name__ == '__main__':
    node1 = Node(3)
    node1.next = Node(30)
    node1.next.next = Node(15)
    node1.next.next.next = Node(9)
    node1.next.next.next.next = Node(6)
    print("Node 1 looks like: ")
    print_nodes(node1)
    
    print("After Merge Sort")
    merge_sort(node1)
    print("Printing Nodes")
    #print_nodes(result)
