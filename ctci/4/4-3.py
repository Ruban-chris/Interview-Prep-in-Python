# Given a binary tree, design an algorithm which creates a linked list of all the
# nodes at each depth.  If you have a tree with depth D, you'll have D linked lists.

# binary tree node
class BinaryTreeNode:
    def __init__(self, obj):
        self.key = obj
        self.left = None
        self.right = None
    def __str__(self):
        return self.key
    def setValue(self, obj):
        self.key = obj
    def setLeft(self, node):
        self.left = node;
    def setRight(self, node):
        self.right = node
    def getValue(self):
        return self.key
    def getLeft(self):
        return self.left
    def getRight(self):
        return self.right

# depth first search
def depthFirstSearch(node):
    if node is not None:
        depthFirstSearch(node.getLeft())
        depthFirstSearch(node.getRight())
        print(node.getValue())
    else:
        return

def depthFirstTreeToLinkedList(node):
    def depthFirstTreeToLinkedListHelper(node, depth, listOfLists):
        if node is not None:
            if depth >= len(listOfLists):
                listOfLists.append([])
            listOfLists[depth].append(node.getValue())
            depthFirstTreeToLinkedListHelper(node.getLeft(), depth + 1, listOfLists)
            depthFirstTreeToLinkedListHelper(node.getRight(), depth + 1, listOfLists)
    listOfLists = []
    depthFirstTreeToLinkedListHelper(node, 0, listOfLists)
    return listOfLists

# breadth first search
def breadthFirstSearch(node):
    queue = []
    queue.append(node)

    while len(queue) > 0:
        nextObj = queue[0]
        if nextObj is not None:
            if nextObj.getLeft() is not None:
                queue.append(nextObj.getLeft())
            if nextObj.getRight() is not None:
                queue.append(nextObj.getRight())
            value = queue.pop(0).getValue()
            print(value)

def breadthFirstTreeToLinkedList(node):
    listOfLists = []
    queue = []
    depth = 0
    
    nodeDepthObj = {
        "node": node,
        "depth": depth
    }
    queue.append(nodeDepthObj)
    
    while len(queue) > 0:
        nextObj = queue.pop(0)
        # build the list
        if nextObj["depth"] >= len(listOfLists):
            listOfLists.append([])
        listOfLists[nextObj["depth"]].append(nextObj["node"].getValue())
        
        if nextObj["node"].getLeft() is not None:
            leftNode = nextObj["node"].getLeft()
            queue.append({
                "node": leftNode,
                "depth": nextObj["depth"] + 1
            })
        if nextObj["node"].getRight() is not None:
            rightNode = nextObj["node"].getRight()
            queue.append({
                "node": rightNode,
                "depth": nextObj["depth"] + 1
            })
        
    
    return listOfLists
            
    
a = BinaryTreeNode('a')
b = BinaryTreeNode('b')
c = BinaryTreeNode('c')

d = BinaryTreeNode('d')

e = BinaryTreeNode('e')
f = BinaryTreeNode('f')
g = BinaryTreeNode('g')

d.setLeft(b)
d.setRight(f)

b.setLeft(a)
b.setRight(c)

f.setLeft(e)
f.setRight(g)

# depthFirstSearch(d)
# breadthFirstSearch(d)
# print(depthFirstTreeToLinkedList(d))
print(breadthFirstTreeToLinkedList(d))
