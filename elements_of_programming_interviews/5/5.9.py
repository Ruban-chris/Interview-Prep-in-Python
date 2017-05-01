# decimal integer is a palindrome

import math

def decimalIntegerPalindrome(integer):
    if integer < 0: return False
    while integer > 0:
        order = math.floor(math.log10(integer))
        print('order', order)
        mask = 10 ** order
        greatestDigit = integer // mask
        smallestDigit = integer % 10
        if greatestDigit != smallestDigit:
            return False
        integer = integer % mask
        integer = integer // 10
    return True

def simple_test():
    assert False == decimalIntegerPalindrome(-1)
    assert True == decimalIntegerPalindrome(0)
    assert True == decimalIntegerPalindrome(123321)
    assert True == decimalIntegerPalindrome(1235321)

def main():
    simple_test()

if __name__ == '__main__':
    main()
