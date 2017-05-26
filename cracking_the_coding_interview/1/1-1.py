# Time complexity O(n) where n is number of characters in string
# Space complexity O(k) where k is number of unique characters in string
def is_unique(string):
    string_set = set()
    for char in string:
        if char in string_set:
            return False
        else:
            string_set.add(char)
    return True

assert(is_unique('asd1234567f'))
assert(False == is_unique('asd1234567ff'))


# Time complexity O(nlogn)
# Space complexity O(1)
def is_unique_2(string):
    stringAsArray = list(string)
    stringAsArray.sort()
    lastChar = None
    for char in stringAsArray:
        if char == lastChar:
            return False
        else:
            lastChar = char
    return True

assert(is_unique_2('asd1234567f'))
assert(False == is_unique_2('asd1234567ff'))
