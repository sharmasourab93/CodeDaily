"""
Python: Singly Linked List
        Program to Check if a given singly linked list has a
        cycle or not.
        Time Complexity: O(N/2)
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
        

# has_cycle Method checks
# if the Linked List has a cycle or not.
def has_cycle(head):
    
    first = second = head
    
    while first.next and second.next:
        if first.next.data == second.data:
            return 1
        
        first = first.next.next
        second = second.next
    
    return 0
    

if __name__ == '__main__':
    node1 = Node(1)
    #print_nodes(node1)
    print(has_cycle(node1))
    
    node2 = Node(1)
    node2.next = Node(2)
    node2.next.next = Node(3)
    node2.next.next.next = node2.next
    # print_nodes(node2)
    print(has_cycle(node2))
