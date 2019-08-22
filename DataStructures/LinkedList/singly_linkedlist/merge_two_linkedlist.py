"""
Python: Linked List
		Merge two sorted Linked List
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def append_list(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head

        while last.next:
            last = last.next

        last.next = new_node


    def merge_lists(self, node1, node2):
        pass


if __name__ == '__main__':

    list1 = LinkedList()
    list1.append_list(10)
    list1.append_list(20)
    list1.append_list(30)
    list1.append_list(40)
    list1.append_list(50)