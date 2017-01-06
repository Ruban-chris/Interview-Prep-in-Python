# Palindrome permutation
# string 
# permutation of a palindrome

# example
# input: Tact Coa
# Output: true (permutations: "taco cat" "atco cta")

# O(n) time
# O(1) space

def isPermutationOfPalindrome(string):
    # count the number of characters excluding spaces
    numberOfNonSpaceChars = 0
    dictionary = {}
    for char in string:
        if char is not ' ':
            numberOfNonSpaceChars += 1
            if dictionary.get(char) is not None:
                dictionary[char] += 1
            else:
                dictionary[char] = 1
    
    if numberOfNonSpaceChars % 2 is 0:
        for key in dictionary:
            if dictionary[key] % 2 is not 0:
                return False
    else:
        numberOfKeysThatAreOdd = 0
        for key in dictionary:
            if numberOfKeysThatAreOdd > 1:
                return False
            if dictionary[key] % 2 is not 0:
                numberOfKeysThatAreOdd += 1
    return True

print(isPermutationOfPalindrome('ttt ttta'))
