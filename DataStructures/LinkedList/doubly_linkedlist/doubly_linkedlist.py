"""
Python: Doubly Linked List (DLL)
        Basic DLL Operations
        1. Pushing Items to a DLL
        2. Insert Item After a reference from a DLL in a DLL
        3. Appending Items to a DLL
        4. Deleting a Node from a DLL
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

    # This method inserts a node after
    # a reference node from the linked list.
    def insert_after(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node cannot be NULL")
            return prev_node

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next is not None:
            new_node.next.prev = new_node
            
    # This method appends a node
    # to the end of the list.
    def append(self, data):
        new_node = Node(data)
        temp = self.head
        
        if self.head is None:
            self.head = new_node
            return self.head
            
        while temp.next:
            temp = temp.next
            
        temp.next = new_node
        new_node.prev = temp
        
        return self.head
    
    # This method deletes a node
    # based on the given data
    # in the argument from the list
    def delete_dll(self, data):
        temp, del_temp = self.head, None
        
        if temp is None:
            return temp
        
        if temp.data == data:
            del_temp = temp
            temp = temp.next
            
            if temp is None:
                self.head = None
                
            else:
                self.head = temp
                temp.prev = self.head
            
        while temp and temp.next.data != data:
            temp = temp.next
        
        del_temp = temp.next
        temp.next = del_temp.next
        del_temp.next.prev = temp
        del_temp.next = del_temp.prev = None
        del del_temp

        return self.head

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
    head_list.append(6)
    head_list.push(7)
    head_list.push(1)
    head_list.append(4)
    print("\nCreated Doubly Linked List")
    DoublyLinkedList.print_list(head_list.head)
    
    print("\nInserting 8 after 7")
    head_list.insert_after(head_list.head.next, 8)
    DoublyLinkedList.print_list(head_list.head)
    
    print("\nDeleting a Node in DLL")
    head_list.delete_dll(7)
    DoublyLinkedList.print_list(head_list.head)
