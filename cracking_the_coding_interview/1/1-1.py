def isUniqueWithDictionary(string):
    obj = {}
    for char in string:
        value = obj.get(char, None)
        if value is None:
            obj[char] = ''
        else:
            return False
    return True

# def isUniqueWithSet(string):

# def isUniqueWithNoAdditionalDataStructures():

# hints
# bit vector 
# O(nlogn)

# do that n times divide the string by 2

# n >> nlogn
# asjglhqia
# O(nlog(n) aaghijlqs
# O(n)
# nlog(n)
# a == a
# a == g
# g == h
# h == i
# i == j
# j == l
# l == q
# q == s
# 
# sort
# acbda
# 
# aabcd
# 
# a [a,b] [c,d]

# for nmber of character in string 
#     string is cut in half
    
    
# [0101010, 010101010, 01010, 0100101]


# 
# startingPoint = 0
# 
# for char in string:
#     for i starting at startingPoint less than string length:
#         if char == string[i]:
#             return False
#         else
#             index++
#     startingPoint++
# return True