class Node:
	def __init__(self,data):
		self.data=data
		self.next=None
class LinkedList:
	def __init__(self):
		self.head=None
	
	def push(self,data):
		node=Node(data)
		if self.head==None: 
			self.head=node
		else:
			temp=self.head
			self.head=node
			node.next=temp
	
	def reverse(self,head,k):
		current=head
		next=None
		prev=None
		count=0
		while current is not None and count<k:
    		next=current.next
    		current.next=prev
    		prev=current
    		current=next
    		count+=1
    	if next is not None:
    		head.next=self.reverse(next,k)
    	return prev
    
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

    def rotation(node,k):
    temp=node
    t1=node
    for i in range(k):
        p_node,temp=pop(node)
        while temp.next is not None:
            temp=temp.next
        temp.next=p_node

"""def rotation(node,k):
    temp=node
    t1=None
    t2=t1
    while k>0 and temp is not None:
        t1.next=temp
        temp=temp.next
        k-=1
    t1.next=None
    kthnode=temp
    while temp is not None:
        temp=temp.next
    temp.next=t2
    while t2 is not None:
        temp=temp.next
        temp.next=t2.next
    return node"""
	
	def printList(self,head):
		temp=head
		while temp is not None:
			print(temp.data)
			temp=temp.next
if __name__=='__main__':
	llist=LinkedList()
	print("Linked list 1",end="\n")
	llist.push(10)
	llist.push(20)
	llist.push(30)
	llist.push(45)
	llist.push(75)
	llist.push(85)
	llist.push(95)
	llist.push(65)
	llist.push(55)
	llist.push(25)
	llist.printList(llist.head)
	print("\nPrinting the reverse",end="\n")
	x=llist.reverse(llist.head,4)
	printList(x)


"""class Node:
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
    llist.printL()"""
        
