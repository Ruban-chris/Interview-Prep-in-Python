# permutations without dupes
# write a method to compute all permutations of a stringWithNoDupes of unique characters.

# the permutations of abc are the permutations of bc with a inserted into every position of the stringWithNoDupes

def permutationWithoutDupes(stringWithNoDupes):
    if len(stringWithNoDupes) is 1: return [stringWithNoDupes]
    firstCharacter = stringWithNoDupes[:1]
    
    stringWithNoDupes = stringWithNoDupes[1:]

    return generatePermutationsWithAdditionalCharacter(firstCharacter, permutationWithoutDupes(stringWithNoDupes))


def generatePermutationsWithAdditionalCharacter(characterToAdd, permutations):
    results = []
    for permutation in permutations:
        for i in range(len(permutation) + 1):
            new_permutation = permutation[:i] + characterToAdd + permutation[i:]
            results.append(new_permutation)
    return results

print(permutationWithoutDupes('abcd'))