"""
Python: Singly Linked List
        Detect & Remove Loops in a linked list
"""


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

    def remove_loop(self, loop_node):

        ptr1 = self.head
        ptr2 = loop_node

        while 1:

            while ptr2.next != loop_node and ptr2.next != ptr1:
                ptr2 = ptr2.next

            if ptr2.next == ptr1:
                break

            ptr1 = ptr1.next

        ptr2.next = None

    # TODO: Fix Detect Loop method
    def detect_loop(self):

        slow_p = fast_p = self.head

        while slow_p and fast_p and fast_p.next:

            slow_p = slow_p.next
            fast_p = fast_p.next.next

            if slow_p == fast_p:
                self.remove_loop(slow_p)
                return 1

        return 0


if __name__ == '__main__':
    first = LinkedList()
    first.push(10)
    first.push(4)
    first.push(15)
    first.push(20)
    first.push(50)

    first.head.next.next.next.next.next = first.head.next.next

    if first.detect_loop() == 1:
        print("Loop detected & removed")
        first.print_list()

    else:
        print("Loop not detected")