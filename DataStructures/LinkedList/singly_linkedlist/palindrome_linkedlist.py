"""
Python: Singly Linked List
        Find if a given linked list is a palindrome.
        
        1. You can either reverse the linked list and check
                if two linked lists match
        2. You can use stack
        3. Measure the length (N) and, traverse n -i times
                at every iterations
"""
from copy import deepcopy


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_nodes(head):
    temp = head
    while temp:
        print(temp.data)
        temp = temp.next
        

# Method to reverse a linked list
# O(N)
def reverse_linkedlist(head):
    temp = deepcopy(head)
    next_, prev, curr = None, None, temp
    
    while curr:
    
        next_, curr.next = curr.next, prev
        prev, curr = curr, next_
    
    temp = prev
    
    return temp


# Driver function which invokes reverse_linkedlist and
# traverses both the lists,
# (given list and reversed list) parallely.
def check_palindrome(head):
    temp = temp1 = head
    temp1 = reverse_linkedlist(temp1)
    
    while temp and temp1:
        
        if temp.data == temp1.data:
            temp = temp.next
            temp1 = temp1.next
            
        else:
            return False
        
    if temp is None and temp1 is None:
        return True
    
    return False


# Check If linked list is palindrome
# Using stack
# Time Complexity O(N) + O(N)
# Auxillary space O(N)
def check_palindrome_stack(head):
    stack = []
    temp = temp1 = head
    
    # Iterating to fill stack
    while temp:
        stack.append(temp.data)
        
        temp = temp.next
    
    # Iterating to compare
    # Stack's top element vs
    # Linked List's data.
    while temp1:
        s = stack.pop()
        
        if temp1.data == s:
            temp1 = temp1.next
        else:
            return False
        
    return True
    
    
if __name__ == '__main__':
    node1 = Node(1)
    node1.next = Node(2)
    node1.next.next = Node(3)
    node1.next.next.next = Node(2)
    node1.next.next.next.next = Node(1)
    
    print("Using Reversal", check_palindrome(node1))
    print("Using Stack", check_palindrome_stack(node1))
