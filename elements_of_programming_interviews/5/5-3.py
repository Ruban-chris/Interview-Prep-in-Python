# Time complexity O(n) where n is the size of the bitword
def reverse_bit_word(bit_word):
    reversed = 0
    while bit_word:
        reversed <<= 1
        reversed |= bit_word & 1
        bit_word >>= 1
    return reversed

assert(0b1101101101 == reverse_bit_word(0b1011011011))

# we can improve reverseBitword by swapping bits i and j instead of going through it one by one

# O(n/2)
def swap_bits(bit_word, i, j):
    if (bit_word & (1 << i)) >> i != (bit_word & (1 << j)) >> j:
        bit_word ^= 1 << i
        bit_word ^= 1 << j
    return bit_word

assert swap_bits(0b101111, 1, 4) == 0b111101
assert swap_bits(0b11100, 0, 2) == 0b11001

def reverse_bit_word_improved(bit_word, bit_word_size):
    i, j = 0, bit_word_size - 1
    while i < j:
        bit_word = swap_bits(bit_word, i, j)
        i += 1
        j -= 1
    return bit_word

assert(0b1101101101 == reverse_bit_word_improved(0b1011011011, 10))


# Time complexity O(size * 2 ** size)
def generate_reverse_look_up_table(size):
    return [reverse_bit_word_improved(bit_word, size) for bit_word in range(1 << size)]

LOOK_UP = generate_reverse_look_up_table(16)

# Time complexity O(n/L) where n is size of word and L is size of mask
def reverse64BitWord(x):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    a = LOOK_UP[(x >> (MASK_SIZE * 3)) & BIT_MASK]
    b = LOOK_UP[(x >> (MASK_SIZE * 2)) & BIT_MASK] << MASK_SIZE
    c = LOOK_UP[(x >> MASK_SIZE) & BIT_MASK] << MASK_SIZE * 2
    d = LOOK_UP[x & BIT_MASK] << MASK_SIZE * 3
    return a | b | c | d

assert reverse64BitWord(64) == reverse_bit_word_improved(64, 64)
assert reverse64BitWord(35327) == reverse_bit_word_improved(35327, 64)
