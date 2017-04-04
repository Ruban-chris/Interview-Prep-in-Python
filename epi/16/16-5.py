import copy
def generatePowerSet(myset):
    if len(myset) == 0:
        return set([set()])
    else:
        poppedEl = myset.pop()
        generatedSets = generatePowerSet(myset)
        result = set()
        for generatedSet in generatedSets:
            result.add(generatedSet)
            result.add(copy(generatedSet).add(poppedEl))
        return result

print(generatePowerSet(set([0,1,2])))