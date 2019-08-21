"""
Python: Stack Data Structure Operation
        Reversing a Stack
"""


class Stack:
    """ Class Stack operations """

    def __init__(self):
        self.stack = []

    def push(self, key):
        self.stack.append(key)

    def pop(self):
        s = self.stack.pop()
        return s

    def print_stack(self):
        print(self.stack)

    # Reverse stack utility method
    def insert_bottom(self, item):
        if len(self.stack) == 0:
            self.push(item)

        else:
            temp = self.pop()
            self.insert_bottom(item)
            self.push(temp)

    # Using recursion to reverse
    def reverse_stack(self):

        if not len(self.stack) == 0:
            temp = self.pop()
            self.reverse_stack()
            self.insert_bottom(temp)

    # Using in-built reverse method in list
    def reverse_method(self):
        return self.stack.reverse()


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
    print("Reversing stack using recursive reverse method")
    s.reverse_stack()
    print(s.stack)
    print("Reversing stack using Default reverse method")
    s.reverse_method()
    print(s.stack)