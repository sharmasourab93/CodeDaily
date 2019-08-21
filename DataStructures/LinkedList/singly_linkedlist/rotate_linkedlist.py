"""
Python: Singly Linked list
        Rotate a linked list
"""


class Node:
				def __init__(self, data):
								self.data = data
								self.next = None
								

class LinkedList:
				
				def __init__(self):
								self.head = None
								
				def push(self, data):
								
								new_data = Node(data)
								new_data.next = self.head
								
								self.head = new_data
								
				
				def rotate_list(self, k):
								count = 0
								current = self.head
								temp1 = self.head
								hold = None
								
								while current is not None and count < k - 1:
												current = current.next
												count += 1
								
								hold = current.next
								current.next = None
								self.head = hold
								temp = hold
								
								while temp.next is not None:
												temp = temp.next
								
								temp.next = temp1
								

				def print_list(self):
								
								temp = self.head
								
								while temp:
												print(temp.data, end="->")
												temp = temp.next
								
								print()
								

if __name__ == '__main__':
				first = LinkedList()
				
				for i in [60, 50, 40, 30, 20, 10]:
								first.push(i)
								
				print("Printing linked List")
				first.print_list()
				
				k = 2
				print("After rotating by {} times".format(k))
				first.rotate_list(k)
				first.print_list()