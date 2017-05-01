# You are given a binary tree in which each node contains an integer value
# (which might be positive or negative). Design an alogorithm to count the number
# of paths that sum to a given value. THe path does not need to start or end at
# the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

class BinaryTreeNode:
    def __init__(self, obj):
        self.data = obj
        self.right = None
        self.left = None
    def setData(self, obj):
        self.data = obj
    def setRight(self, node):
        self.right = node
    def setLeft(self, node):
        self.left = node

node3 = BinaryTreeNode(3)
node4 = BinaryTreeNode(5)
node5 = BinaryTreeNode(5)

node6 = BinaryTreeNode(5)

node7 = BinaryTreeNode(5)
node8 = BinaryTreeNode(5)
node9 = BinaryTreeNode(0)
nodeMinus10 = BinaryTreeNode(-10)
node10 = BinaryTreeNode(10)

node6, node4
node6, node8
node6, node8,


node6.setLeft(node4)
node6.setRight(node8)

node4.setLeft(node3)
node4.setRight(node5)

node8.setLeft(node7)
node8.setRight(node9)
node9.setRight(nodeMinus10)
nodeMinus10.setRight(node10)

def numOfSummationPaths(node, total):
    if node is None:
        return 0
    return numOfSummationPathsHelper(node, total, 0) + numOfSummationPaths(node.left, total) + numOfSummationPaths(node.right, total)

def numOfSummationPathsHelper(node, total, runningTotal):
    if node is None:
        return False
    runningTotal += node.data
    if runningTotal is total:
        return 1 + numOfSummationPathsHelper(node.left, total, runningTotal) + numOfSummationPathsHelper(node.right, total, runningTotal)
    else:
        return numOfSummationPathsHelper(node.left, total, runningTotal) + numOfSummationPathsHelper(node.right, total, runningTotal)

print(numOfSummationPaths(node6, 10))

