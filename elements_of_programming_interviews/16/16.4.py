# generate the power set

import copy

deduplicateArray

def powerSet(array):
    if len(array) == 0:
        return [set()]
    poppedEl = array.pop()
    subsets = powerSet(array)
    result = []
    for subset in subsets:
        result.append(subset)
        subsetCopy = copy.copy(subset)
        subsetCopy.add(poppedEl)
        result.append(subsetCopy)
    return result

print(powerSet([0,1,2,2]))
