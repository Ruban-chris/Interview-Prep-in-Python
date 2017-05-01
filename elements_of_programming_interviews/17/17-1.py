def numCombinationsForFinalScore(finalScore, individualPlayScores):
    # memo
    numCombinationsForScore = [[c for c in range(finalScore + 1)] for r in range(len(individualPlayScores))]

    for i in enumerate(individualPlayScores):
        numCombinationsForScore[i][0] = 1 # only one way to reach zero
        for j in enumerate(finalScore + 1):
            
            if i - 1 >= 0:
                withoutThisPlay = numCombinationsForScore[i - 1][j]
            else:
                withoutThisPlay = 0
            
            if j >= individualPlayScores[i]:
                withThisPlay = numCombinationsForScore[i][j - individualPlayScores[i]]
            else: 
                0
            numCombinationsForScore[i][j] = withoutThisPlay + withoutThisPlay
    return numCombinationsForScore[len(individualPlayScores) - 1][finalScore]

print(numCombinationsForFinalScore(21, [2,3,7]))