"""
Python: Singly Linked List
		Reverse A Linked List
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
								
				# To insert after a specified position
				def insert_after(self, pos, data):
								
								temp = self.head
								new_node = Node(data)
								
								for count in range(pos):
												temp = temp.next
												
								temp1 = temp.next
								temp.next = new_node
								new_node.next = temp1
				
				# To insert towards the end
				def insert_end(self, data):
								new_node = Node(data)
								
								last = self.head
								
								while last.next:
												last = last.next
												
								last.next = new_node
								
				# To Delete key from a linked list
				def delete_key(self, pos):
								new_node = self.head
								
								if pos == 0:
												new_node = new_node.next
												self.head = new_node
												
								elif pos > 0:
												count = 0
												while count < pos-1 and new_node.next:
																new_node = new_node.next
																count += 1
												
												new_node.next = new_node.next.next
				
				# To Print the linked list
				def print_list(self):
								print("Printing Linked list")
								temp = self.head
								while temp:
												print(temp.data, end="->")
												temp = temp.next
								
								print()
				
				# Reverse a given linked list
				def reverse_list(self):
								"""
								  1. Declare three nodes:
									   i. prev = NULL
									  ii. next = NULL
									 iii. current = head

								  2. While iterating over current node
									   i.   set next node as current.next
									  ii.   set current.next as prev
									 iii.   prev as current node
									  iv.   current node as next node.

								  3. Set head as prev and return head
								"""
								
								next_node, prev_node = None, None
								curr_node = self.head
								
								while curr_node is not None:
												next_node = curr_node.next
												curr_node.next = prev_node
												
												prev_node, curr_node = curr_node, next_node
												
								self.head = prev_node
				

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
				print("After Deleting key 0")
				# Printing the linked list after delete operation
				linked_list.print_list()
				print("After deleting key 2")
				linked_list.delete_key(2)
				
				# Printing the linked list after delete operation
				linked_list.print_list()
				linked_list.reverse_list()
				print("After reversing list")
				linked_list.print_list()
				linked_list.delete_key(1)
				print("After deleting key 1 again")
				#Printing the linked list after delete operation
				linked_list.print_list()