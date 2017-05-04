# Swap bits

# input binary number and indices i,j.
# output binary number with bits at positions i,j swapped.

def getBit(number, i):
    return 1 if ((number & (1 << i)) != 0) else 0

def setBit(number, i, ):
    return number | (1 << i)

def clearBit(number, i):
    mask = ~(1 << i)
    return number & mask

def swapBits(number, i, j):
    ithBit = getBit(number, i)
    jthBit = getBit(number, j)
    if ithBit == jthBit: return
    if ithBit == 1:
        number = clearBit(number, i)
        number = setBit(number, j)
    else:
        number = clearBit(number, j)
        number = setBit(number, i)
    return number

print(swapBits(10, 0,1))
