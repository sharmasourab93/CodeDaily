"""
Python: Singly Linked List
        Swapping Nodes without swapping data
"""


class Node:
				def __init__(self, data):
								self.data = data
								self.next = None
								

class LinkedList:
				
				def __init__(self):
								self.head = None
				
				# Push nodes into linked list
				def push(self, data):
								new_node = Node(data)
								
								new_node.next = self.head
								self.head = new_node
				
				# Swap nodes between x & y
				# without swapping data
				# TODO: Correcting Swap nodes
				def swap_node(self, x, y):
								print("#Debug 1")
								temp1, temp2 = self.head, self.head
								
								while temp1:
												if temp1.next.data != x:
																temp1 = temp1.next
								
								print("#Debug 2")
								
								while temp2:
												if temp2.next.data != y:
																temp2 = temp2.next
								
								# Pointing to nodes with data
								# pointing to x & y
								temp_x, temp_y = temp1.next, temp2.next
								print("#Debug 3")
								# Holding the next values
								# to remain intact after swap
								temp3 = temp1.next.next
								temp4 = temp2.next.next
								
								# Swapping & assigning next values
								print("#Debug 4")
								# For temp x
								temp1.next = temp_y
								temp1.next.next = temp3
								
								# For temp y
								temp2.next = temp_x
								temp2.next.next = temp4
								print("#Debug 5")
								
				# Printing list
				def print_list(self):
								print("Printing linked list")
								temp = self.head
								
								while temp:
												print(temp.data, end="->")
												temp = temp.next
												
								print()
												

if __name__ == '__main__':
				
				first_list = LinkedList()
				
				first_list.push(10)
				first_list.push(12)
				first_list.push(30)
				first_list.push(13)
				first_list.push(20)
				first_list.push(14)
				
				x, y = 20, 12
				
				print("Linked list before swapping")
				first_list.print_list()
				
				print("Linked list after swapping {}, {}"
										.format(x, y))
				first_list.swap_node(x, y)
				first_list.print_list()