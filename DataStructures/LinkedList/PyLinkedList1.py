class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def insertAfter(self,pos,data):
        temp=self.head
        new_node=Node(data)
        for count in range (0,pos):
            temp=temp.next
        temp1=temp.next
        temp.next=new_node
        new_node.next=temp1
    def insertLast(self,data):
        new_node=Node(data)
        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node
    def deleteKey(self,pos):
        new_node=self.head
        if(pos==0):
            new_node=new_node.next
            self.head=new_node
        elif(pos>0):
            for count in range(0,pos-1):
                new_node=new_node.next
            new_node.next=new_node.next.next
            
    def printL(self):
        print("Printing List")
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
if __name__=='__main__':
    llist=LinkedList()
    llist.push(3)
    llist.insertLast(4)
    llist.insertAfter(1,20)
    llist.push(5)
    llist.push(6)
    llist.printL()
    llist.deleteKey(0)
    llist.printL()
    llist.deleteKey(2)
    llist.printL()
    llist.deleteKey(1)
    llist.printL()
        
