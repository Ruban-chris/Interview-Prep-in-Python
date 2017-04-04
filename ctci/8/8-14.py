# Given a boolean expression consisting of the symbols 0, 1, &, |, and ^, and 
# a desired boolean results value result, implement a function to count the number
# of ways of parenthesizing the expression such that it evaluates to result.
# The expression should be fully parenthesized eg (0)^(1) but not extraneously.

# EXAMPLE
# countEval("1^0|0|1", false) -> 2
# countEval("0&0&0&1^1", true) -> 10

def countEval(booleanExpression, boolean):
    return countEvalHelper(booleanExpression, boolean, 0)

def countEvalHelper(booleanExpression, boolean, index):
    if index is len(booleanExpression) - 1:
        booleanExpression = balanceParens(booleanExpression)
        print('booleanExpression', booleanExpression, eval(booleanExpression))
        return eval(booleanExpression)
    
    booleanExpressionWithAddedLeftParen = insertLeftParen(booleanExpression, index)
    booleanExpressionWithAddedRightParen = insertRightParen(booleanExpression, index)
    
    result = countEvalHelper(booleanExpression, boolean, index + 1)
    if canAddLeftParen(booleanExpression, index):
        result += countEvalHelper(booleanExpressionWithAddedLeftParen, boolean, index + 2)
    if canAddRightParen(booleanExpression, index):
        result += countEvalHelper(booleanExpressionWithAddedRightParen, boolean, index + 2)
    return result

def insertLeftParen(booleanExpression, index):
    return booleanExpression[:index] + '(' + booleanExpression[index:]

def insertRightParen(booleanExpression, index): 
    return booleanExpression[:index] + ')' + booleanExpression[index:]

def canAddLeftParen(booleanExpression, index):
    if booleanExpression[index] is "1" or booleanExpression[index] is "0":
        return True
    else:
        return False

def canAddRightParen(booleanExpression, index):
    numOfRightParensLessThanLeftParens = booleanExpression.count(')') < booleanExpression.count('(')
    if index > 0:
        numPrecedesCurrentIndex = booleanExpression[index - 1] is "0" or booleanExpression[index - 1] is "1"
    else:
        numPrecedesCurrentIndex = False
    
    if numOfRightParensLessThanLeftParens and numPrecedesCurrentIndex:
        return True
    else:
        return False

def balanceParens(booleanExpression):
    numRightParens = booleanExpression.count(')')
    numLeftParens = booleanExpression.count('(')
    
    while numRightParens != numLeftParens:
        booleanExpression = booleanExpression + ')'
        numRightParens += 1
    return booleanExpression

print(countEval("0&0&0&1^1", True))
print(countEval("1^0|0|1", False))