# my shitty non working implementation
import copy
# Write an algorithm to print all ways of arranging eight queens on an 8x8 chess
# board so that none of them share the same row, columnm or diagonal, In this
# case, diagonal means all diagonals, not just the two that bisect the board.

# [set([(r1,c1), (r2,c2)]), set([(r3,c3), r4,c4])]
# list of sets of queen position tuples

def nQueensOnBoardSafely(n):
    # guard case
    if n is 0:
        return []
    memo = [-1] * (n + 1)
    return nQueensOnBoardSafelyHelper(n, memo)

def nQueensOnBoardSafelyHelper(n, memo):
    # base case
    if n is 0:
        return []
    if memo[n] is not -1:
        return memo[n]
    else:
        memo[n] = addQueenSafely(nQueensOnBoardSafelyHelper(n - 1, memo))
    return memo[n]

def addQueenSafely(queenTupleSets):
    # base case for adding a queen to an empty board
    if len(queenTupleSets) is 0:
        for r in range(0,8):
            for c in range(0,8):
                queenTupleSets.append(set([(r,c)]))
        return queenTupleSets
    else:
        queenTupleSetsWithNewQueen = []
        
        for queenTupleSet in queenTupleSets:
            safeRows = [x for x in range(0,8)]
            safeCols = [x for x in range(0,8)]
            for queenTuple in queenTupleSet:
                safeRows.remove(queenTuple[0])
                safeCols.remove(queenTuple[1])
                for r in safeRows:
                    for c in safeCols:
                        if queenIsSafe((r,c), queenTupleSet):
                            queenTupleSetWithNewQueen = copy.copy(queenTupleSet)
                            queenTupleSetWithNewQueen.add((r,c))
                            queenTupleSetsWithNewQueen.append(queenTupleSetWithNewQueen)
        return queenTupleSetsWithNewQueen
                    
                
    # for each list of queen positions
    # for each open position on the board
        # check if a new queen would be in danger
            
# queenTuple is (r,c), queenTupleSet is set([(r1,c1), (r2,c2)])
def queenIsSafe(queenTupleToAdd, queenTupleSet):
    # guard case
    if len(queenTupleSet) is 0:
        return True
    for queenTuple in queenTupleSet:
        inDangerRow = queenTuple[0] is queenTupleToAdd[0]
        inDangerCol = queenTuple[1] is queenTupleToAdd[1]
        inDangerDiagonally = abs(queenTuple[0] - queenTupleToAdd[0]) == abs(queenTuple[1] - queenTupleToAdd[1])
        if inDangerRow or inDangerCol or inDangerDiagonally:
            return False
    return True

print(nQueensOnBoardSafely(4))