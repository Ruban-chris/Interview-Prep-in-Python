import math

def swap_bits(x, i, j):
    if (x >> i) & 1 != (x >> j) & 1:
        bit_mask = 1 << i | 1 << j
        x ^= bit_mask
    return x

# EPI solution is better.  TODO review this.
def closest_same_weight(x):
    i = 0
    j = None
    n = int(math.log(x, 2) // 1)
    while i <= n and j is None:
        if (x >> i) & 1 == 1:
            if i > 0:
                if (x >> (i - 1)) & 1 == 0:
                    j = i - 1
                    break
            if (x >> (i + 1)) & 1 == 0:
                j = i + 1
                break
        i += 1
    return swap_bits(x, i, j)


assert closest_same_weight(6) == 5
assert closest_same_weight(7) == 11
assert closest_same_weight(2) == 1
assert closest_same_weight(32) == 16
assert closest_same_weight(2**64 - 2) == 2**64 - 3
