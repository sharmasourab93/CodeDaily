"""
Python: Singly Linked List
        Intersection Point Of Two Linked List
        There are 3 ways to do it:
        1. Get Count of the nodes and then based on reference
            get the Intersection Point.
            Time Complexity: O(M + N)
        2. Tweak the Node's structure and mark a visited node
            for every traversal
            Time Complexity: O(M + N)
        3. Use Two loops to traverse and
            find the intersection point.
            Time Complexity: O(M * N)
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
    

def get_count(head):
    """
    get_count traverses a linked list and
    counts the nodes in the Linked List.
    :param head: Linked list
    :return: count of nodes in the linked list
    """
    temp = head
    count = 0
    while temp:
        count += 1
        temp = temp.next
        
    return count


def find_intersection(node1, node2):
    """
    Find_intersection method is meant for
    Finding the common intersecting point
    :Time Complexity: O(M) + O(N),
    where M and N are lengths of Node 1 and node2 respectively.
    :param node1: Linked List 1
    :param node2: Linked List 2
    :return: -1 if intesection is None else Node.data
    """
    temp1, temp2 = node1, node2
    
    count1, count2 = get_count(node1), get_count(node2)
    
    
    diff = abs(count1 - count2)
    d1 = count1 - diff
    c1 = 0
    while temp1 and c1 < d1:
        temp1 = temp1.next
        # print(temp1.data)
        c1 += 1
    
    d2 = count2 - diff
    c2 = 0
    while temp2 and c2 < d2:
        temp2 = temp2.next
        # print(temp2.data, "*")
        c2 += 1
        
    if temp2.data == temp1.data:
        
        return temp1.data
    
    else:
        return -1
    

if __name__ == '__main__':
    node1 = Node(3)
    node1.next = Node(6)
    node1.next.next = Node(9)
    node1.next.next.next = Node(15)
    node1.next.next.next.next = Node(30)
    print("Node 1 looks like: ")
    print_nodes(node1)
    
    node2 = Node(10)
    node2.next = node1.next.next.next
    print("Node 2 looks like: ")
    print_nodes(node2)

    print("Intersection in the above linked lists")
    result = find_intersection(node1, node2)
    print(result)
