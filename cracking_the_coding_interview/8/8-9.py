# Implement an algorithm to print all valid (e.g properly opened and closed)
# combinations of n pairs of parentheses.
# Example

def parenCombinations(n):
    if n is 1: return set(['()'])
    return addParensToParenCombinations(parenCombinations(n - 1))

def addParensToParenCombinations(parenCombinations):
    updatedParenCombinations = set([])
    for parenCombination in parenCombinations:
        for i in range(len(parenCombination)):
            newParenCombination = parenCombination[:i] + '()' + parenCombination[i:]
            updatedParenCombinations.add(newParenCombination)
    return updatedParenCombinations

print(parenCombinations(4))