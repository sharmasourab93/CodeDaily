"""
Python: Doubly Linked List (DLL)
        Remove Duplicates From a DLL
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
    
    # This method inserts a node to
    # the top/first node of the list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        new_node.prev = None
        
        if self.head is not None:
            self.head.prev = new_node
        
        self.head = new_node
    
    # This method removes the duplicate node
    # by undergoing delete operation.
    def remove_duplicates_util(self, head, del_node):
        if head is None:
            return head
        
        temp = head
        
        while temp.next != del_node:
            temp = temp.next
        
        temp.next = del_node.next
        if temp.next is not None:
            temp.next.prev = temp
        
        del_node.next = del_node.prev = None
        del del_node
        
    # This method is the primary driver method for
    # iterating over a sorted/reverse sorted linked list
    # and removing duplicates.
    def remove_duplicates(self, head):
        if head is None:
            return head
        
        current = head
        
        while current.next:
            if current.data == current.next.data:
                self.remove_duplicates_util(head, current.next)
                
            else:
                current = current.next

    @staticmethod
    def print_list(node):
        temp, last = node, None
    
        while temp is not None:
            print(temp.data, end="->")
            last = temp
            temp = temp.next
    
        print()
                

if __name__ == '__main__':
    head_list = DoublyLinkedList()
    head_list.push(1)
    head_list.push(1)
    head_list.push(1)
    head_list.push(1)
    head_list.push(2)
    head_list.push(3)
    head_list.push(3)
    head_list.push(3)
    head_list.push(4)
    head_list.push(5)
    head_list.push(5)
    
    print("Created DLL")
    DoublyLinkedList.print_list(head_list.head)
    
    print("After removing duplicates")
    head_list.remove_duplicates(head_list.head)
    DoublyLinkedList.print_list(head_list.head)
