"""
Python: Doubly Linked List
        Reversing a Doubly Linked List
        1. Iterative Approach
        2. Recursive Approach
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
    
    # This method inserts a node to the first/top node.
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        new_node.prev = None
        
        if self.head is not None:
            self.head.prev = new_node
        
        self.head = new_node

    # This method reverses the Doubly linked list iteratively.
    def iterative_reverse(self):
        current, temp = self.head, None

        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:
            self.head = temp.prev
            
    # This method reverse the Doubly Linked list recursively.
    def recursive_reverse(self, node):
        if node is None:
            return node

        node.next, node.prev = node.prev, node.next
        
        if not node.prev:
            return node
        
        return self.recursive_reverse(node.prev)

    @staticmethod
    def print_list(node):
        temp, last = node, None
    
        while temp is not None:
            print(temp.data, end="->")
            last = temp
            temp = temp.next
    
        print()
        while last:
            print(last.data, end="<-")
            last = last.prev


if __name__ == '__main__':
    head_list = DoublyLinkedList()
    head_list.push(1)
    head_list.push(2)
    head_list.push(3)
    head_list.push(4)
    print("\nCreated Doubly Linked List:")
    DoublyLinkedList.print_list(head_list.head)
    
    print("\nAfter Iterative Reverse")
    head_list.iterative_reverse()
    DoublyLinkedList.print_list(head_list.head)
    
    print("\nAfter Recursive Reverse")
    new_head = head_list.recursive_reverse(head_list.head)
    DoublyLinkedList.print_list(new_head)
