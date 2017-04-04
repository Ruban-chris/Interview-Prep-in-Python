# Write an algorith to find the next node in-order successor of a given node in 
# a bst. you may assume that each node has a link to its parent.

class BinaryTreeNode:
    def __init__(self, obj):
        self.value = obj
        self.left = None
        self.right = None
        self.parent = None
    def getValue(self):
        return self.value
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right
    def getParent(self):
        return self.parent
    def setParent(self, obj):
        self.parent = obj
    def setValue(self, obj):
        self.value = obj
    def setLeft(self, obj):
        self.left = obj
    def setRight(self, obj):
        self.right = obj

node1 = BinaryTreeNode(1)
node2 = BinaryTreeNode(2)
node3 = BinaryTreeNode(3)

node4 = BinaryTreeNode(4)

node5 = BinaryTreeNode(5)
node6 = BinaryTreeNode(6)
node7 = BinaryTreeNode(7)
node8 = BinaryTreeNode(8)
node9 = BinaryTreeNode(9)

node1.setParent(node4)
node2.setParent(node1)
node3.setParent(node2)

node4.setParent(None)

# node5.setParent(node6)
# node6.setParent(node4)
# node7.setParent(node8)
# node8.setParent(node6)
# node9.setParent(node8)

node4.setLeft(node1)
node1.setRight(node2)
node2.setRight(node3)
# node4.setRight(node6)
# 
# 
# node2.setLeft(node1)
# node2.setRight(node3)
# 
# node6.setLeft(node5)
# node6.setRight(node8)
# 
# node8.setLeft(node7)
# node8.setRight(node9)

def findSuccessorOfNode(node):
    if node.getRight() is None:
        possibleSuccessor = node.getParent()
        while possibleSuccessor is not None: 
            if possibleSuccessor is None:
                return None
            if possibleSuccessor.getValue() > node.getValue():
                return possibleSuccessor
            else:
                possibleSuccessor = possibleSuccessor.getParent()
        return None
    else:
        possibleSuccessor = node.getRight()
        
        while possibleSuccessor is not None:
            if possibleSuccessor.getLeft() is not None:
                possibleSuccessor = possibleSuccessor.getLeft()
            else:
                return possibleSuccessor

print(findSuccessorOfNode(node3cc).getValue())

def leftMostChild(node):
    if node is None:
        return None
    while node.getLeft() is not None:
        node = node.getLeft()
    return node

def inOrderSucc(node):
    if node is None:
        return None
    
    # found right children. return leftmost node of right subtree
    if (node.getRight() is not None):
        return leftMostChild(node.getRight())
    else:
        current = node
        parent = current.parent
        while(parent is not None and parent.getLeft() is not current):
            