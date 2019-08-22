"""
Python: Doubly Linked List
        Reverse a doubly linked list
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        temp = Node(data)
        temp.next = self.head

        if self.head is not None:
            self.head.prev = temp

        self.head = temp

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next

    def reverse_list(self):

        temp = None
        current = self.head

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:
            self.head = temp.prev


if __name__ == '__prev__':
    dll = DLinkedList()

    dll.push(2)
    dll.push(4)
    dll.push(8)
    dll.push(10)
    print("Printing after push")
    dll.print_list()
    print("Printing After reversing...")
    dll.reverse_list()
    dll.print_list()

