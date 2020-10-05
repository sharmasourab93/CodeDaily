"""
Python: Singly Linked List
        Detect & Remove Loops in a linked list
"""

global loop_p


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):

        new_node = Node(data)
        new_node.next = self.head

        self.head = new_node

    def print_list(self):
        temp = self.head

        while temp:
            print(temp.data, end="->")
            temp = temp.next

        print()
        
    def detech_remove_loop(self):
        
        temp, hold = self.head, 0
        stack = list()
        stack.append(temp)
        
        while temp.next != self.head:
            hold = temp
            temp = temp.next
            if temp not in stack:
                stack.append(temp)
                
            else:
                del stack
                return hold.next, hold
        
        del stack
        return self.head, None
        


if __name__ == '__main__':
    first = LinkedList()
    first.push(10)
    first.push(4)
    first.push(15)
    first.push(20)
    first.push(50)
    
    first.print_list()
    first.head.next.next.next.next.next = first.head.next.next
    hold_start, hold_end = first.detech_remove_loop()
    
    if hold_end is not None:
        print("Loop found between Node{0} and Node{1}"
              .format(hold_start.data, hold_end.data))
        
        print("Removing Loop")
        hold_end.next = None
        first.print_list()
        
    print("No Loops found.")
    first.print_list()
