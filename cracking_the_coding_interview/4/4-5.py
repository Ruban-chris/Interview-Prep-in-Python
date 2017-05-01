## i made two mistakes.  i did n't know the definition of bst.  left <= node < right
## also ALL nodes to the left of the node must be less than or equal.
## ALL nodes to the right of the node must be greater than or equal.

class BinaryTreeNode:
    def __init__(self, obj):
        self.value = obj
        self.leftChild = None
        self.rightChild = None
    def setLeftChild(self, node):
        self.leftChild = node
    def setRightChild(self, node):
        self.rightChild = node
    def setValue(self, obj):
        self.value = obj
    def getLeftChild(self):
        return self.leftChild
    def getRightChild(self):
        return self.rightChild
    def getValue(self):
        return self.value

node1 = BinaryTreeNode(1)
node2 = BinaryTreeNode(2)
node3 = BinaryTreeNode(3)

node4 = BinaryTreeNode(4)

node5 = BinaryTreeNode(5)
node6 = BinaryTreeNode(6)
node7 = BinaryTreeNode(7)
node8 = BinaryTreeNode(8)
node9 = BinaryTreeNode(9)


node4.setLeftChild(node2)
node4.setRightChild(node6)

node2.setLeftChild(node1)
# node2.setRightChild(node3)

node6.setLeftChild(node5)
node6.setRightChild(node8)

node8.setLeftChild(node7)
node8.setRightChild(node9)


def isValidBSTHelper(node, minValue, maxValue):
    if node is None:
        return True
    if (minValue is not None and n.value <= minValue) || (maxValue is not None and n.value > maxValue):
        return False
    if not(checkBST(n.getLeftChild(), minValue, n.getValue())) or not(checkBST(n.getRightChild(), n.getValue(), maxValue)):
        return False
    return True

def isValidBST(node):
    isValidBSTHelper(node, None, None)

