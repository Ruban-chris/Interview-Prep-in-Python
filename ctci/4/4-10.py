# T1 and T2 are two very large binary trees, with T1 much bigger than T2.
# Create an algorithm to determine if T2 is a subtree of T1.
# A tree T2 is a subtree of T1 if there exists a node n in T1 such that the
# subtree of n is identical toT2. That is, if you cut off the tree at node n,
# the two trees would be identical.

class BinaryTreeNode:
    def __init__(self, obj):
        self.data = obj
        self.right = None
        self.left = None
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

node8Copy = BinaryTreeNode(8)
node9Copy = BinaryTreeNode(9)
node7Copy = BinaryTreeNode(7)


node8Copy.setRight(node9Copy)
node9Copy.setLeft(node7Copy)


def isSubtree(t1Root, t2Root):
    # gc
    if t1Root is None:
        return False
    if t2Root is None:
        return True
    
    def treeToString(tree):
        if tree is None:
            return 'EmptyNode'
        return str(tree.data) + treeToString(tree.left) + treeToString(tree.right)
        
    t1String = treeToString(t1Root)
    t2String = treeToString(t2Root)
    
    # check if the string representation of t2 is a substring of t1
    isSubtree = t2String in t1String
    return isSubtree

print(isSubtree(node6, node8Copy))

