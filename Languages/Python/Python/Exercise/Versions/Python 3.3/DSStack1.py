import sys
class stack1():
    def _init_(self):
        "self declarations"
        self.top=top
        self.stack=[]
        self.x=x
        self.maxlen=maxlen
        

    def _init_(self,option):
        "self declarations"
        self.option=option
      
        
    def pop(self):
        "For Popping all the elements"
        if len(self.stack)<= 0:
            print("Stack Underflow!")
            return 0
        else:
            return stack.pop()
        
    def push(self):
        "For Pushing all the elements"
        if len(self.stack)>= self.maxlen:
            print('Stack Overflow!')
        else:
            p=input("Enter the element to push")
            self.stack.append(p)
            print(p + "Pushed.")
        
        
    def listelements(self):
        "For listing all elements in the stack"
        for i in range(self.maxlen,1):
            print(self.stack[i])
        
    def peep(self):
        'For listing the top element'
        print(len(self.stack))
        
    def option(self):
        "For opting a better option"
        maxlen=input("Enter the maximum length of the stack:")
        while(True):
            print("\nSelect your choice:\n\t1.Push\n\t2.Pop\n\t3.Display\n\t4.Peep")
            xy=input("Enter your Choice:")
            if (xy==1):
                "Push Operation"
                push()
            elif(xy==2):
                "pop operation"
                pop()
            elif(xy==3):
                "Display operation"
                listelements()
            elif(xy==4):
                "Peeping at the top element of the stack"
                peep(maxlen)
            else:
                exit()
        
x=stack1()
x.option()
