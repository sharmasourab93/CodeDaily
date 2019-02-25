"""
Python: Stack Data Structure Operation
							 Reversing a Stack
"""


class Stack:
				""" Class Stack operations """
				def __init__(self):
								"""

								:rtype: list
								"""
								self.stack = []
								
				def push(self, key):
								self.stack.insert(0, key)
				
				def pop(self, index=0):
								s = self.stack.pop(index)
								return s
								
				def print_stack(self):
								print(self.stack)
								
				def reverse_stack(self):
								if len(self.stack) != 0:
												stacked_element = self.pop()
												self.reverse_stack()
												self.push(stacked_element)
				
				def reverse_method(self):
								#print(list(self.stack).reverse())
								return list(self.stack.reverse())
								

if __name__ == "__main__":
				s = Stack()
				s.push(7)
				s.push(8)
				s.push(6)
				s.push(5)
				s.push(4)
				print("Printing stack after push operations")
				print(s.stack)
				print("Using Pop operation")
				s.pop()
				print(s.stack)
				print("Reversing stack using static reverse method")
				s.reverse_stack()
				print(s.stack)
				print("Reversing stack using Default reverse method")
				s.reverse_method()
				print(s.stack)