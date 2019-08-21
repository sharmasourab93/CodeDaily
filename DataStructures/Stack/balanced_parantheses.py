"""
Python: Stack
        Check for balanced parantheses
        
        Time Complexity: O(n)
        Auxiliary Space: O(n) for stack
"""


class Stack:
				
				def __init__(self):
								
								self.stack = []
								
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
								
				def check_balance(self, characters):
								
								for i in range(len(characters)):
												
												if characters[i] in ('[', '{', '('):
																
																self.push(characters[i])
																continue
																
												if len(self.stack) == 0:
																return False
																
												if characters[i] == ')':
																x = self.pop()
																
																if x == '{' or x == '[':
																				return False
																
												elif characters[i] == '}':
																x = self.pop()
																
																if x == '(' or x == '[':
																				return False
																
												elif characters[i] == ']':
																x = self.pop()
																
																if x == '{' or x == '(':
																				return False
								
								if self.is_empty() is True:
												return True
								
								else:
												return False
								

if __name__ == '__main__':
				
				stack = Stack()
				string = ["[()]{}{[()()]()}", "[(])"]
				for i in string:
								
								if stack.check_balance(list(i)) is True:
												print("Expression {} is Balanced".format(i))
								
								else:
												print("Expression {} is Not Balanced".format(i))