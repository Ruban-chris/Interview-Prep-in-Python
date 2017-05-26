# Given two strings, write a method to decide is one is a permutation of the other.

# Ideas
# guard case check the length of both strings

# Idea 1
# we can sort both strings and see if they are equal Time: O(nlogn) Space: O(1)

# Idea 2
# We can keep a dictionary of counts for one string and decrement for the other string.
# Time: O(n) Space(k) where k is number of unique characters in string1 and string2

def are_permutations_1(string1, string2):
    if len(string1) != len(string2):
        return False
    string1AsList = list(string1)
    string1AsList.sort()
    string2AsList = list(string2)
    string2AsList.sort()
    return string1AsList == string2AsList

assert(are_permutations_1('qwerty', 'ytrewq'))
assert(False == are_permutations_1('qwertyf', 'ytrewqs'))


def are_permutations_2(string1, string2):
    if len(string1) != len(string2):
        return False
    character_counts = {}
    for char in string1:
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    for char in string2:
        if char in character_counts:
            character_counts[char] -= 1
        else:
            return False

    for key,value in character_counts.items():
        if value != 0:
            return False
    return True

assert(are_permutations_2('qwerty', 'ytrewq'))
assert(False == are_permutations_2('qwertyf', 'ytrewqs'))
