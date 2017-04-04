def preOrderTraversal(node):
    if node is None:
        return
    else:
        print(node)
        preOrderTraversal(node.left)
        preOrderTraversal(node.right)
    
def inOrderTraversal(node):
    if node is None:
        return
    else:
        inOrderTraversal(node.left)
        print(node)
        inOrderTraversal(node.right)

def postOrderTraversal(node):
    if node is None:
        return
    else:
        postOrderTraversal(node.left)
        postOrderTraversal(node.right)
        print(node)