"""
Python: Circular Linked List
        Split a Circular Linked List into Half.
"""


from circular_linkedlist import CircularLinkedList


class HalfSplitCircularLinkedList(CircularLinkedList):
    
    def get_length(self, node):
        
        temp = node
        count = 0

        while temp != node:
            count += 1
            print(temp.data)
            temp = temp.next
            
        return count
    
    def split_into_half(self):
        
        if self.head is None:
            print("Can't split an empty list.")
            return
        
        if self.head.next == self.head:
            
            print("Can't split 1 node in the list")
            return
        
        fast_ptr = slow_ptr = self.head
        if fast_ptr.next.next == slow_ptr:
            print("First split:")
            print(fast_ptr.data)
            print("Second split:")
            print(slow_ptr.next.data)
            return
           
        slow_ptr = fast_ptr = self.head
        
        while fast_ptr.next != self.head:
            
            if fast_ptr.next.next == self.head:
                fast_ptr = fast_ptr.next
                break
                
            fast_ptr = fast_ptr.next.next
            slow_ptr = slow_ptr.next
        
        llist1, llist2 = fast_ptr.next, slow_ptr.next
        slow_ptr.next, fast_ptr.next = llist1, llist2
        
        temp, temp1 = llist1, llist2
        
        print("Printing First Split, Llist1:")
        while True:
            print(temp.data, end="->")
            temp = temp.next
            if temp == llist1:
                break
        
        print("\nPrinting Second Split, Llist2:")
        while True:
            print(temp1.data, end="->")
            temp1 = temp1.next
            if temp1 == llist2:
                break
        

if __name__ == '__main__':
    llist_ = HalfSplitCircularLinkedList()
    
    llist_.push_in_cll(1)
    llist_.push_in_cll(2)
    llist_.push_in_cll(3)
    llist_.push_in_cll(4)
    #llist_.push_in_cll(5)
    
    print("Printing Linked List Structure")
    llist_.print_list()
    
    print("\nSplitting the linked list")
    llist_.split_into_half()
