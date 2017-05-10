class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

node_a = Node(1)
node_b = Node(0)
node_c = Node(0)
node_d = Node(0)
node_e = Node(1)
node_f = Node(1)
node_g = Node(1)
node_h = Node(0)
node_i = Node(1)
node_j = Node(0)
node_k = Node(0)
node_l = Node(1)
node_m = Node(1)
node_n = Node(0)
node_o = Node(0)
node_p = Node(0)

node_a.left = node_b
node_a.right = node_i
node_b.left = node_c
node_b.right = node_f
node_c.left = node_d
node_c.right = node_e
node_f.right = node_g
node_g.left = node_h
node_i.left = node_j
node_i.right = node_o
node_o.right = node_p
node_j.right = node_k
node_k.left = node_l
node_l.right = node_m
node_k.right = node_n

my_tree = node_a

def binary_sum_helper(tree, numbers, cur_num_str):
    if tree is None:
        return
    if tree.left is None and tree.right is None:
        cur_num_str += str(tree.data)
        numbers.append(cur_num_str)
        return
    cur_num_str += str(tree.data)
    if tree.left:
        binary_sum_helper(tree.left, numbers, cur_num_str)
    if tree.right:
        binary_sum_helper(tree.right, numbers, cur_num_str)


def binary_sum(tree):
    numbers = []
    binary_sum_helper(tree, numbers, '')
    sum = 0
    for number in numbers:
        sum += int(number, 2)
    return sum

assert(126 == binary_sum(my_tree))
