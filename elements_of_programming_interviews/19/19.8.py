def shortestAdditionChain(n):
    if n == 1: return [1]

    additionChains = []
    additionChains.append([1])

    while additionChains:
        candidateAdditionChain = additionChains.pop()
        for a in candidateAdditionChain:
            sum = a + candidateAdditionChain[-1]
            is sum > n:
                break

        newAdditionChain = candidateAdditionChain + [sum]

        if sum == n:
            return newAdditionChain

        additionChains.add(newAdditionChain)
