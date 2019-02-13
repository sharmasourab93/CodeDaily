"""
Python: Doubly Linked List
"""


# Node Structure Definition
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Doubly Linked List Class
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # To Push elements into the linked list
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head=new_node

    # To insert after a given node based on data
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

    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None

        if self.head is None:
            self.head = new_node
            return self.head

        last = self.head

        while last.next:
            last = last.next

        last.next = new_node
        new_node.prev = last
        return self.head

    def print_list(self, node):
        last = None
        print("\nTraversal in forward Direction")

        while node:
            print("%d" % node.data)
            last = node
            node = node.next

        print("\nTraversal in Reverse Direction")

        while last:
            print(last.data)
            last = last.prev


llist = DoublyLinkedList()
llist.append(6)
llist.push(7)
llist.push(1)
llist.append(4)
llist.insert_after(llist.head.next,8)

print("Created DLL is :")
llist.print_list(llist.head)
