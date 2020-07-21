"""
Python: Singly Linked List
        Find length of the loop in a linked List.
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


# Finding the Legth of the loop.
# Best Case O(N)
# Worst O(N * M), where m is the
# number of nodes in the loop.
def loop_length(head):
    if head is None:
        return 0
    
    slow, fast = head, head
    
    # Just an extra condition layer to
    # ensure we are only traversing a linked list
    # containing loop
    if has_cycle(head):
        flag = 0
        while slow and slow.next and fast and \
                fast.next and fast.next.next:
            
            if slow == fast and flag != 0:
                # If this condition matches
                # Then loop exists
                count = 1
                slow = slow.next
                
                # Bring Slow to pace
                # On loop detection
                while slow != fast:
                    slow = slow.next
                    count += 1
                    
                return count
            
            slow = slow.next
            fast = fast.next.next
            flag = 1
        
        return 0


# has_cycle Method checks
# if the Linked List has a cycle or not.
def has_cycle(head):
    first = second = head
    
    while first.next and second.next:
        if first.next.data == second.data:
            return True
        
        first = first.next.next
        second = second.next
    
    return False


if __name__ == '__main__':
    node1 = Node(1)
    node1.next = Node(2)
    node1.next.next = Node(3)
    node1.next.next.next = Node(4)
    node1.next.next.next.next = Node(5)
    node1.next.next.next.next.next = node1.next
    print(loop_length(node1))
