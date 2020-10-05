"""
Python: Circular Linked List (CLL)

"""


class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        

class CircularLinkedList:
    
    def __init__(self):
        self.head = None
    
    # Pushing items into a Circular Linked list
    def push_in_cll(self, data):
        
        ptr1 = Node(data)
        temp = self.head
        
        # Condition 1. if Head is None
        if self.head is None:
            self.head = ptr1
            ptr1.next = self.head
            return
        
        ptr1.next = self.head
        
        # Condition 2: If Head is not None
        # While Iterator's next is not equal to Head
        if self.head is not None:
            while temp.next != self.head:
                temp = temp.next
                if temp.next == self.head:
                    break
            temp.next = ptr1
            
        self.head = ptr1
    
    # Prints the Circular Linked list
    # While breaking away on the loop.
    def print_list(self):
        
        if self.head is None:
            print(" No Nodes to traverse/iterate over.")
            return

        temp = self.head
        
        while True:
            if self.head is not None:
                print("{0}".format(temp.data), end="->")
                temp = temp.next
            
            if temp == self.head:
                break
                
    def delete_node(self, data):
        
        if self.head is None:
            print("Circular list is empty.")
            return
        
        temp = self.head
        
        if temp.data == data:
            del_node = temp
            new_temp = self.head
            
            while new_temp.next != del_node:
                new_temp = new_temp.next
            
            self.head = del_node.next
            new_temp.next = self.head
        
        else:
        
            while temp.next.data != data:
                temp = temp.next
            
            del_node = temp.next
            temp.next = del_node.next
        
        del_node.next = None
        del del_node
        return
            

if __name__ == '__main__':
    llist_ = CircularLinkedList()
    
    # llist_.delete_node(1)
    
    llist_.push_in_cll(1)
    llist_.push_in_cll(2)
    llist_.push_in_cll(3)
    llist_.push_in_cll(4)
    llist_.push_in_cll(5)
    
    print("Printing the list")
    llist_.print_list()
    
    print("\nDeleting node from list")
    llist_.delete_node(1)
    llist_.print_list()
