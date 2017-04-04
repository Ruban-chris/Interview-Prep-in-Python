
# the probability of returning the current node is 1/(number of children + 1)
# the probability of going left is (number of children on the left)/(number of children + 1)
# the probability of going right is (number of children on the right)/(number of children + 1)

# so getting a child from depth 2
#        1
#    2      3
#  4   5   6   7
#        3   4   4

# probability of returning root: 1/7
# probability of return 2: 3/7 * 1/3 = 3/21 = 1/7
# probability of returning 4: 3/7 * 1/3 = 3/21 = 1/7
# probability of returning 5: 3/7 * 1/3 = 3/21 = 1/7

# each node should keep track of the number of children it has on either subtree

class BinaryTreeNode:
    def __init__(self, obj):
        self.left = None
        self.right = None
        self.numOfLeftChildren = 0
        self.numOfLeftChildren = 0
        self.data = obj
    def setData(self, obj):
        self.data = obj
    def setRight(self, node):
        self.numOfRightChildren = node.numOfLeftChildren + node.numOfRightChildren + 1
        self.right = obj
    def setLeft(self, node):
        self.numOfLeftChildren = node.numOfLeftChildren + node.numOfRightChildren + 1
    def insert(self, node):
        # assume the tree is a bst
        # walk the nodes
        # if root in tree is less than node, go right
        # if root is greater than node go left
        # if ther eare not children. insert to the correct location.
        # update the parent num of children property.
    def delete(self, node):
        # use find to locate the node.
        # delete it and update the parent child property.
    def find(self, node):
        # walk the tree to find the node.
        
    def getRandomNode(self):
        if self.left is None and self.right is None:
            return self
        if number is 1:
            return root
        if number > 1 and number <= numOfLeftChildren + 1:
            return getRandomNode(self.left)
        if number > numOfLeftChildren + 1 and number <= numOfLeftChildren + 1 + numOfRightChildren:
            return getRandomNode(self.right)