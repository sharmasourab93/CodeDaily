"""
Python: Doubly Linked List (DLL)
        Quick Sort On Doubly Linked List
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
    @staticmethod
    def get_last(head):
        temp = head
        
        while temp and temp.next:
            temp = temp.next
        
        return temp
    
    # Partition For Pivoting a linked list.
    def partition(self, start, end):
        
        pivot = end.data
        node_i = start
        node_j = start
        
        while node_j is not None:
            
            if node_j.data <= pivot:
                node_i = node_i.next
                node_i.data, node_j.data = node_j.data, node_i.data
            
            node_j = node_j.next
            
        node_i.next.data, pivot = pivot, node_i.next.data
        
        return node_i.next
        
    #TODO: Quick Sort
    def quick_sort(self, start, end):
        pivot = self.partition(start, end)
        self.quick_sort(start, pivot.prev)
        self.print_list(pivot)
        self.quick_sort(pivot.next, end)
        
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
    
    print("Quick Sort On Doubly Linked List")
    end_ = DoublyLinkedList.get_last(head_list.head)
    head_list.quick_sort(head_list.head, end_)
    DoublyLinkedList.print_list(head_list.head)
