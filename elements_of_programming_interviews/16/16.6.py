def generateParens(n):
    if n < 0: return None
    if n == 0: return [""]
    result = []
    generateParensHelper(n, n, result, '')
    return result

def generateParensHelper(numLeftNeeded, numRightNeeded, result, parens):
    if numLeftNeeded == 0 and numRightNeeded == 0:
        result.append(parens)
    if numLeftNeeded > 0:
        generateParensHelper(numLeftNeeded - 1, numRightNeeded, result, parens + '(')
    if numLeftNeeded < numRightNeeded:
        generateParensHelper(numLeftNeeded, numRightNeeded - 1, result, parens + ')')

print(generateParens(3))
