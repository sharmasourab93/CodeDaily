#define a coder constructed stack
class Stack:
    "Stack class"
    def __init_(self):
        self.items=[]
    def isEmpty(self):
        self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        self.items.pop()
    def size(self):
        return len(self.items)
    def main(self):
        "main function"
        while(True):
            print("What do you wish to do?\n")
            print("\t1.Push an element into the stack\n\t2.Pop an element from the stack\n\t3.Size of the stack\n\t4.Check the emptiness")
            option=input("\nEnter your Choice:")
            if(option==1):
                x=input("Enter the element:\n")
                self.push(x)
            elif(option==2):
                self.pop()
            elif(option==3):
                self.size()
            elif(option==4):
                self.isEmpty()
            else:
                return 0

x=Stack()
x.main()

                
