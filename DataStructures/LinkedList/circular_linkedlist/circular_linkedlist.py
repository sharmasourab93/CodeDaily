"""
Python: Circular Linked List (CLL)
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


class CircularLinkedList:
    
    def __init__(self):
        self.last = None
        
    def add_to_empty(self, data):
        
        if self.last is not None:
            return self.last
        
        temp = Node(data)
        self.last = temp
        self.last.next = self.last
        return self.last
    
    def add_to_begin(self, data):
        
        if self.last is None:
            return self.add_to_empty(data)
        
        temp = Node(data)
        temp.next = self.last.next
        self.last.next = temp
        
        return self.last
    
    def add_end(self, data):
        
        if self.last is None:
            return self.add_to_empty(data)
        
        temp = Node(data)
        temp.next = self.last.next
        self.last.next = temp
        self.last = temp
        
        return self.last
    
    def add_after(self, data, item):
        
        if self.last is None:
            return None
        
        temp = Node(data)
        p = self.last.next
        
        while p:
            if p.data == item:
                temp.next = p.next
                p.next = temp
                
                if p == self.last:
                    self.last = temp
                    return self.last
                else:
                    return self.last
            
            p = p.next
            if p == self.last.next:
                print(item, "not present in the list")
                break
    
    def traverse(self):
        if self.last is None:
            print("List is empty")
            return
        
        temp = self.last.next
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
            if temp == self.last.next:
                break

   
if __name__ == '__main__':
    llist = CircularLinkedList()
    
    last = llist.add_to_empty(6)
    last = llist.add_to_begin(4)
    last = llist.add_to_begin(2)
    last = llist.add_end(8)
    last = llist.add_end(12)
    last = llist.add_after(10, 8)
    
    llist.traverse()
