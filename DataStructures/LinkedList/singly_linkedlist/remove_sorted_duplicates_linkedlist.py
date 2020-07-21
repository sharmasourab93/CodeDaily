"""
Python: Singly Linked List
        Remove Duplicated In a Sorted Singly Linked List
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
# duplicates in the linked list.
def non_dup_llist(node1):
    temp = head = node1
    if temp.data == temp.next.data:
        temp.next = delete_node(head, temp.next)
    
    while temp.next and temp.next.next:
        
        if temp.data == temp.next.data:
            temp.next = delete_node(head, temp.next)
        
        elif temp.next.data == temp.next.next.data:
            temp.next.next = delete_node(head, temp.next.next)
            
        temp = temp.next

    return node1
    

if __name__ == '__main__':
    node1 = Node(1)
    node1.next = Node(1)
    node1.next.next = Node(1)
    node1.next.next.next = Node(2)
    node1.next.next.next.next = Node(3)
    node1.next.next.next.next.next = Node(3)
    node1.next.next.next.next.next.next = Node(4)
    node1.next.next.next.next.next.next.next = Node(4)
    
    print("Original Linked List")
    print_nodes(node1)
    result_node = non_dup_llist(node1)
    print("\nResult Node")
    print_nodes(result_node)
