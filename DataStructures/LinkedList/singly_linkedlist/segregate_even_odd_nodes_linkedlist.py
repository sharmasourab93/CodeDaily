"""
Python: Singly Linked List
        Segregate Even and Odd Nodes in a Linked List
"""


class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


def print_nodes(head):
    temp = head
    while temp:
        print(temp.data, end="->")
        temp = temp.next
    print("\n")


#TODO: Segregate Odds
def segregate_odds(head):
    even_start = even_end = None
    odd_start = odd_end = None
    temp = head
    
    while temp:
        val = temp.data
        
        if temp % 2 == 0:
            pass
    

if __name__ == '__main__':
    node1 = Node(3)
    node1.next = Node(6)
    node1.next.next = Node(9)
    node1.next.next.next = Node(15)
    node1.next.next.next.next = Node(30)
    print("Node 1 looks like: ")
    print_nodes(node1)
    
    segregate_odds(node1)
    print_nodes(node1)