
# given a binary search tree generate a list of the of all possible arrays that could have
# generated the bst

class BinaryTreeNode:
    def __init__(self, obj):
        self.data = obj
        self.left = None
        self.right = None
        self.depth = None
    def setData(self, obj):
        self.data = obj
    def setLeft(self, obj):
        self.left = obj
    def setRight(self, obj):
        self.right = obj

# returns an array of arrays that groups the nodes by depth
def treeToArray(root):
    if root is None:
        return None
    root.depth = 0

    treeInArrayForm = []
    queue = []
    queue.append(root)
    
    while len(queue) > 0:
        node = queue.pop(0)
        # add the treeInArrayForm to hold each depth
        if len(treeInArrayForm) <= node.depth:
            treeInArrayForm.append([])
            
        if node.left is not None:
            node.left.depth = node.depth + 1
            queue.append(node.left)
        if node.right is not None:
            node.right.depth = node.depth + 1
            queue.append(node.right)
        treeInArrayForm[node.depth].append(node.data)

    return treeInArrayForm

# bfs but i also want to track depth to build an array of arrays.

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

print('treeToArray(node6)', treeToArray(node6))