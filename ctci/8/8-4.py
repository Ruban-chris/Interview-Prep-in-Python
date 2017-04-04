import copy
# Power set: Write a method to return all subsets of a set.

def allSubsets(mySet):
    if len(mySet) is 0:
        return [set()]

    poppedElement = mySet.pop()
    print('mySet', mySet)
    print('poppedElement', poppedElement)
    subsets = allSubsets(mySet)
    subsetsCopy = copy.deepcopy(subsets)

    for subset in subsetsCopy:
        subset.add(poppedElement)

    result = subsets

    return subsetsCopy + subsets

print(allSubsets(set([1,2,3,4])))