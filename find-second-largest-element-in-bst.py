# Write a function to find the 2nd largest element in a binary search tree

class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

my_tree1 = BinaryTreeNode(3)
my_tree1.insert_left(2)
my_tree1.left.insert_left(1)

my_tree2 = BinaryTreeNode(3)
my_tree2.insert_left(1)
my_tree2.left.insert_right(2)

my_tree3 = BinaryTreeNode(2)
my_tree3.insert_left(1)
my_tree3.insert_right(3)

my_tree5 = BinaryTreeNode(1)
my_tree5.insert_right(2)
my_tree5.right.insert_right(3)

my_tree7 = BinaryTreeNode(8)
my_tree7.insert_right(10)
my_tree7.right.insert_right(14)
my_tree7.right.right.insert_left(13)

my_tree7.insert_left(3)
my_tree7.left.insert_left(1)
my_tree7.left.insert_right(6)
my_tree7.left.right.insert_left(4)
my_tree7.left.right.insert_right(7)

my_tree4 = BinaryTreeNode(1)
my_tree4.insert_right(3)
my_tree4.right.insert_left(2)

def iterativeFindLargestSubTreeInTree(tree):
    largestNode = tree
    while (hasattr(largestNode.right, 'value')):
        largestNode = largestNode.right
    else:
        return largestNode

def recursiveFindLargestSubTreeInTree(tree):
    if not(hasattr(tree.right, 'value')):
        return tree
    else:
        return recursiveFindLargestSubTreeInTree(tree.right)

def findParent(value, tree):
    if value is tree.value:
        print('value is root node')
    if value > tree.value:
        if hasattr(tree.right, 'value'):
            if tree.right.value is value:
                print(tree.value)
            else:
                findParent(value, tree.right)
    if value < tree.value:
        if hasattr(tree.left, 'value'):
            if tree.left.value is value:
                print(tree.value)
            else:
                findParent(value, tree.left)

def findSecondLargestElementInBST(tree):
    largestNode = iterativeFindLargestSubTreeInTree(tree)
    if hasattr(largestNode.left, 'value'):
        print(iterativeFindLargestSubTreeInTree(largestNode.left).value)
    else:
        findParent(largestNode.value, tree)

findSecondLargestElementInBST(my_tree1)
findSecondLargestElementInBST(my_tree2)
findSecondLargestElementInBST(my_tree3)
findSecondLargestElementInBST(my_tree4)
findSecondLargestElementInBST(my_tree5)

findSecondLargestElementInBST(my_tree7)

