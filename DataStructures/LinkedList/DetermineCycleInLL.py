'''Determine Cycle in Linked List'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:

    def __init__(self):
        self.head=None

    def pushNode(self,data):
        newNode=Node(data)
        newNode.next=self.head
        self.head=newNode

    def insertBTW(self,pos,data):
        newNode=Node(data)
        temp=self.head
        if pos==0:
            self.pushNode(data)
        while pos!=0:
            if pos>0:
                pos-=1
                temp=temp.next
            temp1=temp.next
            temp.next=newNode
            temp.next.next=temp1
        
    def popNode(self):
        if self.head.next!=None:
            newNode=self.head
            self.head=self.head.next

    def printlist(self):
        heady=self.head
        print("\nPrinting the linkedList: ",end=" ")
        while heady!=None:
            print(heady.data,end=" ")
            heady=heady.next

    def putCycle(self):
        heady=self.head
        while heady!=None:
            heady=heady.next
        heady.next=self.head

    def detectCycle(self):
        slw=self.head
        fast=self.head
        while slw.data!=None and fast.data!=None:
            if slw.data!=fast.data:
                slw=slw.next
                fast=fast.next.next
        print('No Cycle Detected!')
        

if __name__=='__main__':
    ll=LinkedList()
    ll.pushNode(21)
    ll.pushNode(22)
    ll.printlist()
    ll.popNode()
    ll.pushNode(23)
    ll.pushNode(25)
    ll.insertBTW(2,45)
    ll.pushNode(26)
    ll.printlist()
    #ll.putCycle()
    #ll.detectCycle()
    
    
        
            
        
