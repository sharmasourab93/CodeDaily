"""
Python: Singly Linked List & operations
"""


# Singly Linked List Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # To push node at the beginning of a linked list
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # To push a node after a position of a linked list
    def insert_after(self, pos, data):
        temp = self.head
        new_node = Node(data)

        for count in range(pos):
            temp = temp.next

        temp1 = temp.next
        temp.next = new_node
        new_node.next = temp1

    # To insert towards the end of a linked list
    def insert_end(self, data):
        new_node = Node(data)
        last = self.head

        while last.next:
            last = last.next

        last.next = new_node

    # To delete a node based on position from a linked list
    def delete_key(self, pos):
        print("\n Deleting key", end=" ")
        new_node = self.head

        if pos == 0:
            new_node = new_node.next
            self.head = new_node

        elif pos > 0:
            for count in range(pos-1):
                new_node = new_node.next

            new_node.next = new_node.next.next

    # To Reverse a linked list
    def reverse(self, head):
        """
        1. Declare three nodes:
             i. prev = NULL
             ii. next = NULL
             iii. current = head

        2. While iterating over current node
            i.   set next node as current.next
            ii.  set current.next as prev
            iii. prev as current node
            iv.  current node as next node.

        3. Set head as prev and return head
        """
        next_node = None
        prev_node = None
        current_node = head

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node

        head = prev_node
        return head

    # To print the linked list
    def print_list(self):
        print("\nPrinting List", end=" ")

        temp = self.head

        while temp:
            print(temp.data, end="->")
            temp = temp.next


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.push(3)
    linked_list.insert_end(4)
    linked_list.insert_after(1, 20)
    linked_list.push(5)
    linked_list.push(6)

    # Printing the linked list after insertion
    linked_list.print_list()

    linked_list.delete_key(0)

    # Printing the linked list after delete operation
    linked_list.print_list()

    linked_list.delete_key(2)

    # Printing the linked list after delete operation
    linked_list.print_list()

    linked_list.delete_key(1)

    #Printing the linked list after delete operation
    linked_list.print_list()
        
