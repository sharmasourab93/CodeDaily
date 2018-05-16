class datastructure:
    def __init__(self, data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next

#Code execution starts here
if __name__=='__main__':
    llist=LinkedList()
    llist.head=datastructure(1)
    second=datastructure(2)
    third=datastructure(3)

    llist.head.next=second
    second.next=third
    llist.printList()
    
