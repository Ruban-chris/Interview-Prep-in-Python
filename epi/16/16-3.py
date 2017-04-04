from copy import copy

def genPerm(array):
    if len(array) is 0:
        return [[]]
    else:
        popEl = array.pop()
        genSubPerms = genPerm(array)
        results = []
        for subPerm in genSubPerms:
            for i,char in enumerate(subPerm):
                copiedSubPerm = copy(subPerm)
                copiedSubPerm.insert(i, popEl)
                results.append(copiedSubPerm)
            copiedSubPerm = copy(subPerm)
            copiedSubPerm.append(popEl)
            results.append(copiedSubPerm)
        return results
# print(genPerm([1,2,3]))

# i switched the params of insert
# i thought append() would return the array but it returns none
# i also swapped the positions of enumerate

# book's solution
def permutations(array):
    result = []
    directedPermutations(0, array, result)
    return result

def directedPermutations(i, array, result):
    if i == len(array) - 1:
        result.append(copy(array))
        return
        
    for j in range(i, len(array)):
        # swap it
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
        
        directedPermutations(i + 1, array, result)
        
        # unswap it
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
    
print(permutations([1,2,3]))