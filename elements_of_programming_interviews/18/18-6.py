def findMajorityElement(array):
    majorityThreshold = len(array) // 2 + 1
    print('majorityThreshold', majorityThreshold)
    elementCounts = {}
    
    for el in array:
        if el in elementCounts:
            elementCounts[el] += 1
            if elementCounts[el] >= majorityThreshold:
                return el
        else:
            elementCounts[el] = 1
    print('elementCounts', elementCounts)
    return False

print(findMajorityElement(['b', 'a', 'c', 'a', 'a', 'b', 'a', 'a', 'c', 'a']))
