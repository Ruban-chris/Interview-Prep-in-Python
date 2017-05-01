def construct_from_base(num_as_int, base):
    return ('' if num_as_int == 0 else
            construct_from_base(num_as_int // base, base) +
            string.hexdigits[num_as_int % base].upper())

def convert_base(num_as_string, b1, b2):
    is_negative = num_as_string[0] == '-'
    num_as_int = functools.reduce(
        lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
        num_as_string[is_negative:], 0)
    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else
                                           construct_from_base(num_as_int, b2))



# import math
# def baseConversion(string, b1, b2):
#     mapping = {10: "A", 11: "B", 12: "C", 13:"D", 14: "E", 15: "F"}
#     stringAsList = list(string)
#     isNegative = True if stringAsList[0] is '-' else False
#     if isNegative:
#         stringAsList.pop(0)
#     numberInBase10 = 0
#     for i, digit in enumerate(stringAsList):
#         numberInBase10 += b1 ** (len(stringAsList) - 1 - i) * int(digit)
#     numberInBase2List = []
#     while numberInBase10 > 0:
#         order = math.floor(math.log(numberInBase10, b2))
#         mask = b2 ** order
#         largestB2Digit = numberInBase10//mask if numberInBase10//mask < 10 else mapping[numberInBase10//mask]
#         numberInBase2List.append(str(largestB2Digit))
#         numberInBase10 = numberInBase10 % mask
#     if isNegative:
#         return '-' + ''.join(numberInBase2List)
#     else:
#         return ''.join(numberInBase2List)
#
# def simple_test():
#     assert '2C' == baseConversion('101010', 2, 15)
#     assert '-2C' == baseConversion('-101010', 2, 15)
#     assert '2C' == baseConversion('101010', 2, 15)
#     assert '-1389C4E2' == baseConversion('-2342342342', 8, 16)
#
#
# def main():
#     simple_test()
#
# if __name__ == '__main__':
#     main()


import functools
import sys
import random
import string


def construct_from_base(num_as_int, base):
    return ('' if num_as_int == 0 else
            construct_from_base(num_as_int // base, base) +
            string.hexdigits[num_as_int % base].upper())

def convert_base(num_as_string, b1, b2):
    is_negative = num_as_string[0] == '-'
    f = lambda x, c: x * b1 + string.hexdigits.index(c.lower())

    num_as_int = functools.reduce(f, num_as_string[is_negative:], 0)
    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else
                                           construct_from_base(num_as_int, b2))
