import math
def isBinaryTreeBST(tree):
    return areKeysInRange(tree, -math.inf, math.inf)

def areKeysInRange(tree, lower, upper):
    if tree is None:
        return True
    else if tree.data < lower or tree.data >= upper:
        return False
    
    return areKeysInRange(tree.left, lower, tree.data) and areKeysInRange(tree.right, tree.data, upper)
    
# O(n) time complexity because we call the function n times
# O(h) space complexity because we recurse h times.

        