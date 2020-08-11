"""
Python: Singly Linked List
        Quick Sort On Singly Linked List
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
    

# parition_last method takes in two arguments start & end.
# The method takes the data in the last node as pivot and then
# paritions based on the pivot and
# returns pointer to the partioned node.
def partition_last(start, end):
    # Base condition
    if start == end or not start or not end:
        return start
    
    # pivot_prev is the paritioned node.
    pivot_prev = curr = start
    # pivot holds the data in the last element of the linked list.
    pivot, temp = end.data, int()
    
    while start != end:
        
        if start.data <= pivot:
            pivot_prev = curr
            curr.data, start.data = start.data, curr.data
            curr = curr.next
            
        start = start.next
    
    curr.data, pivot = pivot, curr.data
    end.data = pivot
    
    return pivot_prev
    

def quick_sort(start, end):
    # Base Condition
    if start == end:
        return
    
    # Split list and partition recurse
    pivot_prev = partition_last(start, end)
    quick_sort(start, pivot_prev)
    
    # If pivot is picked and moved to the start
    # that means start and pivot is same
    # so pick from next of pivot
    if pivot_prev is not None and pivot_prev == start:
        quick_sort(pivot_prev.next, end)
        
    # If pivot is in between the list
    # start from next of pivot
    # since we have pivot_prev to move 2 nodes.
    elif pivot_prev is not None and pivot_prev.next is not None:
        quick_sort(pivot_prev.next.next, end)
        

if __name__ == '__main__':
    node1 = Node(3)
    node1.next = Node(30)
    node1.next.next = Node(15)
    node1.next.next.next = Node(9)
    node1.next.next.next.next = Node(6)
    print("Node 1 looks like: ")
    print_nodes(node1)
    
    print("After Quick_sort")
    end_ = node1.next.next.next.next
    quick_sort(node1, end_)
    print_nodes(node1)
