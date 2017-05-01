# Write a program that takes an array A and an index i into A, and rearranges
# the elements such that all elements less than A[i] (the "pivot") appear first,
# followed by elements equal to the pivot, followed by elements greater than the pivot.

def partitionArray(array, i):
    pivot = array[i]
    lessThanPivot = []
    equalToPivot = []
    greaterThanPivot = []
    j = 0
    while j < len(array):
        element = array[j]
        if element < pivot:
            lessThanPivot.append(element)
        elif element > pivot:
            greaterThanPivot.append(element)
        else:
            equalToPivot.append(element)
        j += 1
    result = lessThanPivot + equalToPivot + greaterThanPivot
    return result

myArray = [3,6,1,6,7,4,9,2,6,7,2]
print(partitionArray(myArray, 3))