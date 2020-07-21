"""
Python: Singly Linked List
        Remove Duplicated In a Un-Sorted Singly Linked List
        Two ways of doing it
        1. Using two while loops
        2. Using Sort algorithms and
            removing elements in a sorted list
            
Downside: Maintains the position of the element
    at the first encounter.
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


# Delete Node Method.
# Releases all unwanted loose ends in the linked list
# And returns pointer to next item in the list.
def delete_node(head, delnode):
    temp = head
    
    while temp.next != delnode:
        temp = temp.next
    
    temp.next = delnode.next
    delnode.next = None
    del delnode
    
    return temp.next


# Method which removes
# duplicates in the linked list
# Worst case method O(N ^2)
# Takes 2 while loops to iterate
def non_dup_llist(node1):
    
    temp = head = node1
    
    if temp.data == temp.next.data:
        temp.next = delete_node(head, temp.next)
    
    while temp:
        
        temp1 = temp
        
        while temp1 and temp1.next:
            
            if temp.data == temp1.next.data:
                temp1.next = delete_node(head, temp1.next)
                
            temp1 = temp1.next
            
        temp = temp.next
    
    return node1


if __name__ == '__main__':
    node1 = Node(10)
    node1.next = Node(4)
    node1.next.next = Node(1)
    node1.next.next.next = Node(5)
    node1.next.next.next.next = Node(5)
    node1.next.next.next.next.next = Node(7)
    node1.next.next.next.next.next.next = Node(4)
    node1.next.next.next.next.next.next.next = Node(1)
    
    print("Original Linked List")
    print_nodes(node1)
    result_node = non_dup_llist(node1)
    print("\nResult Node")
    print_nodes(result_node)
