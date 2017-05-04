# Bit-wise Operators

## Two's complement binary for negative integers:
Negative numbers are written with a leading one instead of a leading zero.  Python uses an infinite number of bits to represent numbers.  The number -5 is treated by bitwise operators as if it were written '...1111111111111111111011'

## x << y
Returns x with the bits shifted to the left by y places (and new bits on the right-hand-side are zeros). This is the same as multiplying x by 2 ** y.

## x >> y
Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.

## x & y
Does a "bitwise and".  Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise it's 0.

## x | y
Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise it's 1.

## ~ x
Returns the complement of x - the number you get by switching each 1 for a 0 and each 0 for a 1.  This is the same as -x - 1.

## x ^ y
Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if the bit in y is 0, and its the complement of the bit in x if that bit in y is 1.

# Bit Facts
x ^ 0s = x
x ^ 1s = ~x
x ^ x = 0
x & 0s = 0
x & 1s = x
x & x = x
x | 0s = x
x | 1s = 1s
x | x = x

# Twos Complement
Negative numbers are represented using the two's complement of its absolute value with a 1 in its sign bit to indicate negative value.


For the 4 bit integer -3, we have one bit for the sign and three bits for the value.  We want the complement with respect to 2 ** 3.  The complemenet of 3 is 5.  5 in binary is 101. Therefore, -3 in binary as a 4 bit number is 1101, with the first bit being the sign bit.


Another way to look at this is we invert the bits in the positive representation and then add 1.  3 is 011 in binary. Flip the bigs to get 100, add 1 to get 101, and prepend the sign bit (1) to get 1101.

# Arithmetic vs Logical Right Shift
There are two types of right shift operators.  The arithmetic right shift divides by two.  The logical shift moves all the bits including the sign bit to the right.

If we repeatedly logically shift a number we will get 0.
If we repeatedly arithmetic shift a number, we will get -1 because a sequence of all 1s in a signed integer represents -1.

# Getting and Setting
This method shifts 1 over by i bits, creating a value that looks like 00010000.  By performing and AND with num, we clear all bits other than the bit at bit i. Comparing it with 0 then bit i must have a 1 otherwise bit i is a 0
```py
def getBit(num, i):
  return ((num & (1 << i)) != 0)
```

setBit shifts 1 over by i bits, creating a value like 00010000.  By performing an OR with num, only the value at bit i will change. All other bits of the mask are zero and will not affect num.
```py
def setBit(num, i):
  return num | (1 << i)
```

clearBit creates a number like 11101111, then we perform an AND with num.  This will clear the ith bit.
```py
def clearBit(num, i):
  mask = ~(1 << i)
  return num & mask
```

clearBitsMSBthroughI clears bits from the most significant bit through i (inclusive).  We create a mask with a 1 at the ith bit.  Then we subtract 1 from it, giving us a sequence of 0s followed by i 1s.  We then AND our number with this mask to leave just the last i bits.
```py
def clearBitsMSBthroughI(num, i):
  mask = (1 << i) - 1
  return num & mask
```

To clear all bits from i through 0 (inclusive), we take a sequence of all 1s (which is -1) and shift it left by i + 1 bits.
This gives us a sequence of 1s (in the most significant bits) followed by i 0 bits.
```py
def clearBitsIthrough0(num, i):
  mask = (-1 << (i + 1))
  return num & mask
```

# Update Bit
```py
def updateBit(num, i, bitIs1):
  value = 1 if bitIs1 else 0
  mask = ~(1 << i)
  return (num & mask) | (value << i)
```

x & (x - 1) clears the lowest set bit in x
x & ~(x - 1) extracts the lowest set bit in x.
