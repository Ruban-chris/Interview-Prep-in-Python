foo = [500]
bar = [646]

# using xor
def number_swap(a,b):
    a[0] ^= b[0]
    b[0] ^= a[0]
    a[0] ^= b[0]

# pythonic swap is tuple unpacking: a,b = b,a


number_swap(foo, bar)

assert(foo[0] == 646)
assert(bar[0] == 500)
