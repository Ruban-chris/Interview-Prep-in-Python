class Node:
    def __init__(self, data):
        self.data = data
    def setNext(self, node):
        self.next = node
    def setData(self, data):
        self.data = data

def mergeLists(list1, list2):
    dummyHead = Node(None)
    p1 = list1
    p2 = list2
    current = dummyHead
    
    while p1 is not None and p2 is not None:
        if p1.data <= p2.data:
            current.next = p1
            p1 = p1.next
        else:
            current.next = p2
            p2 = p2.next
        current = current.next
    
    if p1 is None:
        current.setNext(p2)
    else:
        current.setNext(p1)

    return dummyHead.next