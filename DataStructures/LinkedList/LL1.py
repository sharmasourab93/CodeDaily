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
