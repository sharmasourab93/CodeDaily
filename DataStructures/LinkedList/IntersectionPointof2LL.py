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
    '''def find_node(self,data):
        temp=self.head
        while temp.data==data:
            temp=temp.next
        return temp'''
    def printLList(self):
        print("\nPrinting Linked list")
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

if __name__=='__main':
    ll1=LinkedList()
    ll1.push(3)
    ll1.push(6)
    ll1.push(7)
    ll1.push(15)
    ll1.push(30)
    ll2.push(10)
    ll1.printLList()
