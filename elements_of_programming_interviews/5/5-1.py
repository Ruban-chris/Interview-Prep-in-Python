# Solution from EPI
# Brute Force
# O(n) check every bit

def parity1(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

# O(k) check ever set bit. k is the number of 1's

def parity2(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result

# If we precompute the parity for all the numbers from 0 to (2^16 - 1) and put it in a lookup table,
# we can process multiple bits at a time.

PRECOMPUTED_PARITY = [parity1(number) for number in range(1 << 16)]

def parity3(x):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF # this is 16 1's
    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^
            PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^
            PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK] ^
            PRECOMPUTED_PARITY([x & BIT_MASK])
            )

# we can use xor a number with itself to compute parity.
def parity4(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1 # 0x1 is 1 in hexadecimal
