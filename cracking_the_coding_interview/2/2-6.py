from ctci.data_structures.stack import Stack
from ctci.data_structures.node import Node
from ctci.data_structures.unorderedList import UnorderedList

def isllPalindrome(ll):
    # GC:
    if ll.head.getData() is None:
        return False

    # get a pointer and traverse the linked list, putting the values in a stack
    pointer = ll.head
    linkedListStack = Stack()
    while pointer is not None:
        linkedListStack.push(pointer.getData())
        pointer = pointer.getNext()
    
    # set the pointer back to the beginning and traverse the linked list, comparing the value with values off the top of the stack
    pointer = ll.head
    while pointer is not None:
        if pointer.getData() is not linkedListStack.pop():
            return False
        else:
            pointer = pointer.getNext()
    return True
    
    
# A better solution would be to only need to compare the first half.
    
Node1 = Node('c')
Node2 = Node('f')
Node3 = Node('f')
Node4 = Node('a')
Node5 = Node('c')

Node1.setNext(Node2)    
Node2.setNext(Node3)
Node3.setNext(Node4)
Node4.setNext(Node5)

myLinkedList = UnorderedList()
myLinkedList.head = Node1
print(myLinkedList)
print(isllPalindrome(myLinkedList))

