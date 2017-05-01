# A magic index in an array A[0...n-1] is defined to be an index such that
# A[i] = i. Given a sorted array of distinct integers, write a method to find a
# magic index, if one exists, in array A.

# What if the values are not distinct.
import math
my_array = [0, 2, 3, 4, 5, 6, 7, 8]


def magicIndex(array):
    return magicIndexHelper(array, 0)

def magicIndexHelper(array, startingIndex):
    # guard case
    print('array', array)
    roundedMidPoint = len(array) // 2
    
    if len(array) is 1:
        if array[roundedMidPoint] == roundedMidPoint + startingIndex:
            return array[roundedMidPoint]
        else:
            return None
            
    
    if array[roundedMidPoint] == roundedMidPoint + startingIndex:
        return array[roundedMidPoint]
    elif array[roundedMidPoint] > roundedMidPoint + startingIndex:
        return magicIndexHelper(array[:roundedMidPoint], 0)
    elif array[roundedMidPoint] < roundedMidPoint + startingIndex:
        return magicIndexHelper(array[roundedMidPoint:], startingIndex + roundedMidPoint)

print(magicIndex(my_array))


def magicFast(array):
    reurn magicFastHelper(array, 0, len(array) - 1)

def magicFastHelper(array, start, end):
    if (end < start): return -1
    mid  = (start + end) / 2
    if array[mid] == mid:
        return mid
    elif (array[mid] > mid):
        return magicFastHelper(array, start, mid - 1)
    else:
        return magicFastHelper(array, mid + 1, end)


        
    
    