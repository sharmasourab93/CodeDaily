"""
Python: Doubly Linked List (DLL)
        Rotate Doubly Linked List
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
    
    # This method returns the number of nodes in a DLL.
    def get_length(self, head):
        temp = head
        count = 0
        while temp:
            count += 1
            temp = temp.next
            
        return count
    
    # This method rotates the linked list by k
    def rotate(self, k=0):
        n = self.get_length(self.head)
        
        if k >= n:
            k = k - n
            if k - n == 0:
                return self.head
            
        h_temp = k_temp = self.head
        i = 1
        
        while i < k:
            k_temp = k_temp.next
            i += 1
            
        temp = k_temp.next
        self.head = temp
        k_temp.next = None
        
        while temp.next:
            temp = temp.next
            
        temp.next = h_temp
        h_temp.prev = temp
        
        return self.head
    
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
    head_list.push(2)
    head_list.push(3)
    head_list.push(4)
    head_list.push(5)
    head_list.push(6)
    
    print("Created DLL")
    DoublyLinkedList.print_list(head_list.head)
    
    print("Rotate Linked List")
    rotate_num = 1
    head_list.rotate(rotate_num)
    DoublyLinkedList.print_list(head_list.head)
