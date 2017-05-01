class BinaryTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def isSymmetric(tree):
    if tree is None:
        return True
    return ish(tree.left, tree.right)

def ish(left, right):
    if left is None and right is None:
        return True
    elif left is None:
        return False
    elif right is None:
        return False
    else:
        return left.value == right.value and ish(left.right, right.left) and ish(left.left, right.right)

def simple_test():
    print('what')
    symmetric_tree = BinaryTreeNode(5,
                          BinaryTreeNode(4,
                                         BinaryTreeNode(2),
                                         BinaryTreeNode(3,
                                                        BinaryTreeNode(1),
                                                        BinaryTreeNode(0))),
                          BinaryTreeNode(4,
                                         BinaryTreeNode(3,
                                                        BinaryTreeNode(0),
                                                        BinaryTreeNode(1)),
                                         BinaryTreeNode(2))

                          )

    asymmetric_tree = BinaryTreeNode(5,
                          BinaryTreeNode(4,
                                         BinaryTreeNode(2),
                                         BinaryTreeNode(3,
                                                        BinaryTreeNode(1),
                                                        BinaryTreeNode(0))),
                          BinaryTreeNode(4,
                                         BinaryTreeNode(3,
                                                        BinaryTreeNode(0),
                                                        BinaryTreeNode(1)),
                                         BinaryTreeNode(2, BinaryTreeNode(4)))

                          )
    assert True == isSymmetric(symmetric_tree)
    assert False == isSymmetric(asymmetric_tree)
    assert True == isSymmetric(BinaryTreeNode(5))
    assert True == isSymmetric(BinaryTreeNode(5))
    assert False == isSymmetric(BinaryTreeNode(5, BinaryTreeNode(4)))

def main():
    simple_test()

if __name__ is '__main__':
    main()
