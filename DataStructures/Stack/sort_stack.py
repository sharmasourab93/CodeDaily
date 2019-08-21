"""
Python: Stack
        Sort A Stack
"""


class Stack:
				
				def __init__(self):
								
								self.stack = []
				
				def __str__(self):
								return ' '.join(str(self.stack))
								
				def push(self, element):
								
								self.stack.append(element)
				
				def pop(self):
								
								return self.stack.pop()
				
				def top(self):
								
								return self.stack[-1]
				
				def is_empty(self):
								
								if len(self.stack) == 0:
												return True
								
								else:
												return False
					# TODO: Fixing sorted stack
				def sorted_insert(self, element):
								if self.is_empty() or element > self.top():
												self.push(element)
								
								temp = self.pop()
								self.sorted_insert(temp)
								self.push(temp)
												
												
				def sort_stack(self):
								
								if not self.is_empty():
												temp = self.pop()
												self.sort_stack()
												self.sorted_insert(temp)
												

if __name__ == '__main__':
				
				push_list1 = [30, -5, 18, 14, -3]
				
				stack = Stack()
				
				for i in push_list1:
								stack.push(i)
								
				stack.sort_stack()
				print(stack)