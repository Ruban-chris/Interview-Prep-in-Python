# global variable, tracks current subtree
subtreeIdx = None

def reconstructPreorder(preorder):
    subtreeIdx = 0
    return reconstructPreorderSubtree(preorder)
    
def reconstructPreorderSubtree(preorder):
    subtreeKey = preorder[subtreeIdx]
    ++subtreeIdx
    if subtreeKey is None:
        return None
    leftSubtree = reconstructPreorderSubtree(preorder)
    rightSubtree = reconstructPreorderSubtree(preorder)
    return Node(subtreeKey, leftSubtree, rightSubtree)
    
    