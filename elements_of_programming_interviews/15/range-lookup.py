import collections
# idea is recursively traverse the tree

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    def __contains__(self, item):
        if self.start <= item and self.end >= item:
            return True
        else:
            return False

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def return_keys_in_interval(bst, interval):
    results = []
    def return_keys_in_interval_helper(bst, interval, results):
        if bst is None:
            return
        if bst.data in interval:
            results.append(bst.data)

        if bst.data > interval.start:
            return_keys_in_interval_helper(bst.left, interval, results)

        if bst.data < interval.end:
            return_keys_in_interval_helper(bst.right, interval, results)

    return_keys_in_interval_helper(bst, interval, results)

    return results

# Tests

node_a = Node(19)
node_b = Node(7)
node_c = Node(3)
node_d = Node(11)
node_e = Node(19)
node_f = Node(2)
node_g = Node(5)
node_h = Node(17)
node_i = Node(13)
node_j = Node(16)
node_k = Node(23)
node_l = Node(47)
node_m = Node(53)
node_n = Node(37)
node_o = Node(29)
node_p = Node(41)
node_q = Node(31)

node_a.left = node_b
node_a.right = node_e
node_b.left = node_c
node_b.right = node_d
node_c.left = node_f
node_c.right = node_g
node_d.right = node_h
node_h.left = node_i
node_i.right = node_j
node_e.left = node_k
node_e.right = node_l
node_k.right = node_n
node_n.left = node_o
node_n.right = node_p
node_o.right = node_q
node_l.right = node_m

assert all(number in return_keys_in_interval(node_a, Interval(16,31)) for number in [19,17,23,29,31])

# Complexities
# Time O(m + h) Average. O(n) worst case when the interval covers all values in tree
# Space O(k) where k is number of results.
