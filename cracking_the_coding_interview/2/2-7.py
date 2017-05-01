Node1 = Node('a')
Node2 = Node('b')
Node3 = Node('q')
Node4 = Node('d')

Node1.setNext(Node2)
Node2.setNext(Node3)
Node3.setNext(Node4)

list1 = UnorderedList()
list1.head = Node1

NodeY = Node('y')
NodeZ = Node('z')
NodeA = Node('a')
NodeB = Node('b')

NodeY.setNext(NodeZ)
NodeZ.setNext(NodeA)
NodeA.setNext(NodeB)
NodeB.setNext(Node3)

list2 = UnorderedList()
list2.head = NodeY

print('list1', list1)
print('list2', list2)

def returnIntersectingNode(ll1, ll2):
    # guard case
    if ll1.head is None or ll2.head is None:
        return False

    # traverse the first list to the end
    length1 = 0
    runner1 = ll1.head
    while runner1.getNext() is not None:
        runner1 = runner1.getNext()
        length1 += 1

    # traverse the second list to the end
    length2 = 0
    runner2 = ll2.head
    while runner2.getNext() is not None:
        runner2 = runner2.getNext()
        length2 += 1

    # compare the pointers
    if runner1 != runner1:
        return False
    else:
        # return the intersecting node
        # reset both runners and start them the same distance away from the intersecting node
        runner1 = ll1.head
        runner2 = ll2.head
        if length1 > length2:
            while length1 is not length2:
                runner1 = runner1.getNext()
                length1 -= 1
        if length2 > length1:
            while length2 is not length1:
                runner2 = runner2.getNext()
                length2 -= 1

        while runner1 != runner2:
            runner1 = runner1.getNext()
            runner2 = runner2.getNext()

        # return the intersecting node
        return runner1

print(returnIntersectingNode(list1, list2))
