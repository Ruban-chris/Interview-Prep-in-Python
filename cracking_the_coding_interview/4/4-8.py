# i think theres a mistake in book.  what the two nodes are parent/child?
class BinaryTreeNode:
    def __init__(self, obj):
        self.data = obj
        self.left = None
        self.right = None
    def setData(self, obj):
        self.data = obj
    def setRight(self, obj):
        self.right = obj
    def setLeft(self, obj):
        self.left = obj

node3 = BinaryTreeNode(3)
node4 = BinaryTreeNode(4)
node5 = BinaryTreeNode(5)

node6 = BinaryTreeNode(6)

node7 = BinaryTreeNode(7)
node8 = BinaryTreeNode(8)
node9 = BinaryTreeNode(9)

node6.setLeft(node4)
node6.setRight(node8)

node4.setLeft(node3)
node4.setRight(node5)

node8.setLeft(node7)
node8.setRight(node9)


# first common ancestor

def findFirstCommonAncestor(root, node1, node2):
    if root is None:
        return
    
    leftContainsOne = nodeIsDescendant(root.left, node1) and not(nodeIsDescendant(root.left, node2)) or nodeIsDescendant(root.left, node2) and not(nodeIsDescendant(root.left, node1))
    rightContainsOne = nodeIsDescendant(root.right, node1) and not(nodeIsDescendant(root.right, node2)) or nodeIsDescendant(root.right, node2) and not(nodeIsDescendant(root.right, node1))
    leftOrRightContainOneEach = leftContainsOne or rightContainsOne
    
    if leftOrRightContainOneEach:
        return root
    else:
        return findFirstCommonAncestor(root.left, node1, node2) or findFirstCommonAncestor(root.right, node1, node2)
        
def nodeIsDescendant(root, node):
    if root is None:
        return False
    if root is node:
        return True
    leftTree = nodeIsDescendant(root.left, node)
    rightTree = nodeIsDescendant(root.right, node)
    return leftTree or rightTree

print('foo', findFirstCommonAncestor(node6, node7, node9).data)
