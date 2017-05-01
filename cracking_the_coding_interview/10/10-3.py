# Given a sorted array of n integers that has been rotated an unknown number of times,
# write  code to find an element in te=he array.  You may assume that the array was originally sorted in increasing order
def isStrictlyIncreasing(sortedAndRotatedArray):
    if len(sortedAndRotatedArray) < 2:
        return False
    else:
        return sortedAndRotatedArray[0] < sortedAndRotatedArray[len(sortedAndRotatedArray)- 1]

def elementInRange(sortedArray, element):
    if len(sortedArray) is 0:
        return False
    if sortedArray[0] <= element and element <= sortedArray[len(sortedArray) - 1]:
        return True
    else:
        return False


def findElementInRotatedArray(rotatedArray, element):
    return findElementInRotatedArrayHelper(rotatedArray, element, 0, len(rotatedArray) - 1)

def findElementInRotatedArrayHelper(rotatedArray, element, startPointer, endPointer):
    if len(rotatedArray) is 0: return False
    
    midPointer = (endPointer - startPointer) // 2 + startPointer
    leftSide = rotatedArray[startPointer:midPointer]
    rightSide = rotatedArray[midPointer:endPointer]
    print('midPointer', midPointer)
    print('leftSide', leftSide)
    print('rightSide', rightSide)
    
    
    if rotatedArray[midPointer] is element:
        return midPointer
    if rotatedArray[startPointer] is element:
        return startPointer
    if rotatedArray[endPointer] is element:
        return endPointer
    elif isStrictlyIncreasing(leftSide):
        if elementInRange(leftSide, element):
            return findElementInRotatedArrayHelper(rotatedArray, element, startPointer, midPointer)
        else:
            return findElementInRotatedArrayHelper(rotatedArray, element, midPointer, endPointer)
    elif isStrictlyIncreasing(rightSide):
        if elementInRange(rightSide, element):
            return findElementInRotatedArrayHelper(rotatedArray, element, midPointer, endPointer)
        else:
            return findElementInRotatedArrayHelper(rotatedArray, element, startPointer, midPointer)

rotatedArray = [5, 7, 10, 14, 15, 16, 19, 20, 25, 1, 3, 4]
print(findElementInRotatedArray(rotatedArray, 4))

