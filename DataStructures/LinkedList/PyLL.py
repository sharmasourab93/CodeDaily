class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked:
    def __init__(self):
        pass
    def push(self,node,data):
        head=None
        head=node
        if head==None:
            return Node(data)
        
        temp=Node(data)
        temp.next=head
        head=temp
        return head
    def print_(self,node):
        head=node
        while head!=None:
            print(head.data,end="  ")
            head=head.next
    def predef(self):
        H=None
        H=self.push(H,10)
        H=self.push(H,20)
        H=self.push(H,30)
        H=self.push(H,40)
        H=self.push(H,50)
        self.print_(H)
if __name__=='__main__':
    ll=Linked()
    ll.predef()
    
        
