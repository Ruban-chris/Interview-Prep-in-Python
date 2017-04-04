class BinaryTreeNode():
    def __init__(self, obj):
        self.value = obj
        self.rightChild = None
        self.leftChild = None
    def getValue(self):
        return self.value
    def getRightChild(self):
        return self.rightChild
    def getLeftChild(self):
        return self.leftChild
    def setValue(self, object):
        self.value = object
    def setRightChild(self, BinaryTreeNode):
        self.rightChild = BinaryTreeNode
    def setLeftChild(self, BinaryTreeNode):
        self.leftChild = BinaryTreeNode


def checkHeight(node):
    if node is None:
        return -1
    
    leftHeight = checkHeight(node.getLeftChild())
    rightHeight = checkHeight(node.getRightChild())
    
    if (leftHeight is False):
        return False
    
    if (rightHeight is False):
        return False
        
    if abs(leftHeight - rightHeight) > 1:
        return False
    else:
        return max(leftHeight, rightHeight) + 1



a = BinaryTreeNode('a')
b = BinaryTreeNode('b')
c = BinaryTreeNode('c')

d = BinaryTreeNode('d')

e = BinaryTreeNode('e')
f = BinaryTreeNode('f')
g = BinaryTreeNode('g')
h = BinaryTreeNode('h')
i = BinaryTreeNode('i')

d.setLeftChild(b)
d.setRightChild(f)

b.setLeftChild(a)
b.setRightChild(c)

f.setLeftChild(e)
f.setRightChild(g)

g.setRightChild(h)
h.setRightChild(i)

print('d', checkHeight(d))
print('b', checkHeight(b))
print('g', checkHeight(g))
