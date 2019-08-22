"""
Python: Singly Linked List
        Add two numbers represented by linked list
        Time Complexity: O(m + n)
                         where, m & n are number of nodes
                         in first & second list respectively
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_data = Node(new_data)
        new_data.next = self.head

        self.head = new_data


    def add_two_list(self, first, second):

        temp, prev = None, None
        carry = 0

        while first is not None or second is not None:

            fdata, sdata = 0, 0
            sum = 0

            fdata = 0 if first is None else first.data
            sdata = 0 if second is None else second.data
            sum = carry + fdata + sdata

            carry = 1 if sum >= 10 else 0

            sum = sum if sum < 10 else sum % 10

            temp = Node(sum)

            if self.head is None:
                self.head = temp

            else:
                prev.next = temp

            prev = temp

            if first is not None:
                first = first.next

            if second is not None:
                second = second.next

        if carry > 0:
            temp.next = Node(carry)


    def print_list(self):
        # print("Printing list")
        temp = self.head

        while temp:
            print(temp.data, end="->")
            temp = temp.next

        print()


if __name__ == '__main__':
    first = LinkedList()
    second = LinkedList()

    first.push(9)
    first.push(4)
    # first.push(9)
    first.push(5)
    # first.push(7)
    print("Linked List first")
    first.print_list()

    second.push(2)
    second.push(4)
    second.push(8)
    print("Linked List second")
    second.print_list()

    third = LinkedList()
    print("Adding List 1 and list 2")
    third.add_two_list(first.head, second.head)
    third.print_list()