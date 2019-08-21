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

        self.head = new_node

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

    @staticmethod
    def print_list(node):
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


if __name__ == '__main__':
    head_list = DoublyLinkedList()
    head_list.append(6)
    head_list.push(7)
    head_list.push(1)
    head_list.append(4)
    head_list.insert_after(head_list.head.next, 8)

    print("Created DLL is :")
    head_list.print_list(head_list.head)
