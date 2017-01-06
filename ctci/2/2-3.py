class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    def __str__(self):
        return self.getData() + '->'
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata
        
    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:
    def __init__(self):
        self.head = None
    def __str__(self):
        string = ''
        current = self.head
        while current != None:
            string += current.__str__()
            current = current.getNext()
        string += 'None'
        return string
    def size(self):
        return self.head.size()
    def isEmpty(self):
        return self.head == None
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()
        
        return count
    
    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        
        return found
    
    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
    
    def append(self,item):
        current = self.head
        while current != None:
            if current.getData() == None:
                current.setNext(Node(item))
            else:
                current = current.getNext()
    
    def insert(self, item, i):
        idx = 0
        previous = None
        current = self.head
        while idx != i:
            previous = current
            current = current.getNext()
            idx += 1
        
        if previous == None:
            self.head = Node(item)
        else:
            insertedNode = Node(item)
            insertedNode.setNext(current)
            previous.setNext(insertedNode)
    
    # def index(i, item)
    # def pop(i)

# Delete the middle node of a singly linked list.

def deleteMiddleNode(middleNode):
    if middleNode is None or middleNode.next is None:
        return False
    else:
        nextNode = middleNode.getNext()
        middleNode.setData(nextNode.getData())
        middleNode.setNext(nextNode.getNext())

NodeA = Node('a')

NodeB = Node('b')
NodeACopy = Node('a')
NodeC = Node('c')

NodeA.setNext(NodeB)
NodeB.setNext(NodeACopy)
NodeACopy.setNext(NodeC)

myLinkedList = UnorderedList()
myLinkedList.head = NodeA

deleteMiddleNode(NodeACopy)

print(myLinkedList)