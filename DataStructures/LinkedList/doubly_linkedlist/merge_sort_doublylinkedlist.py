"""
Python: Doubly Linked List (DLL)
        Merge Sort On Doubly Linked List
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
    
    # This method merges the list
    def merge(self, first, second):
        
        if first is None:
            return second
        
        if second is None:
            return first
        
        if first.data < second.data:
            first.next = self.merge(first.next, second)
            first.next.prev = first
            first.prev = None
            return first
        
        else:
            second.next = self.merge(first, second.next)
            second.next.prev = second
            second.prev = None
            return second
        
    # Merge sort
    def merge_sort(self, head):
        temp = head
        if temp is None:
            return temp
        
        if temp.next is None:
            return temp
        
        second = self.split(temp)
        
        temp = self.merge_sort(temp)
        second = self.merge_sort(second)
        
        return self.merge(temp, second)
    
    # Splits the linked list
    def split(self, head):
        fast = slow = head
        while True:
            if fast.next is None:
                break
            
            if fast.next.next is None:
                break
                
            fast = fast.next.next
            slow = slow.next
            
        temp = slow.next
        slow.next = None
        return temp
    
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
    
    print("Merge Sort On Doubly Linked List")
    head_ = head_list.merge_sort(head_list.head)
    DoublyLinkedList.print_list(head_)
