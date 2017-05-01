Node1 = Node('1')
Node2 = Node('2')
Node3 = Node('3')
Node4 = Node('4')
Node5 = Node('5')
Node6 = Node('6')
Node7 = Node('7')
Node8 = Node('8')
Node9 = Node('9')

Node1.setNext(Node2)
Node2.setNext(Node3)
Node3.setNext(Node4)
Node4.setNext(Node5)
Node5.setNext(Node6)
Node6.setNext(Node7)
Node7.setNext(Node8)
Node8.setNext(Node9)
Node9.setNext(Node3)

list1 = UnorderedList()
list1.head = Node1

# given a circular linked list, implement an algorithm that returns the node at the beginning of the loop
# return the start of the loop

def returnStartOfCircularLinkedList(ll):
    # guard case
    if (ll.head is None):
        return False

    # increment pointer1 by 1 step until it reaches the end or it collides with pointer2
    # increment pointer2 by 2 steps until it reaches the end or it collides with pointer1
    pointer1 = ll.head
    pointer2 = ll.head
    while True:
        pointer1 = pointer1.getNext()
        pointer2 = pointer2.getNext()
        if pointer2 is not None:
            pointer2 = pointer2.getNext()

        if (pointer1 == pointer2 or pointer1 is None or pointer2 is None): break

    if pointer1 is None or pointer2 is None:
        return False

    # pointer1 and pointer2 have collided in the circle.  They are x number of steps away from the start of the circle.
    # Where x is the length of linked list before the start of the circle.  Create another pointer at the start of
    # the linked list.  Move the new pointer and pointer1 together one step at a time until they collide at the
    # start of the circle.
    pointer0 = ll.head

    while pointer0 != pointer1:
        pointer0 = pointer0.getNext()
        pointer1 = pointer1.getNext()

    # pointer0 is now at the start of the circle.
    return pointer0

print(returnStartOfCircularLinkedList(list1))
