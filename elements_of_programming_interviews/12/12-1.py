# Write a method that takes a sorted array and a key and returns the index of the 
# first occurrence of that key in the array.

def firstOccurenceofK(array, k):
    if len(array) is 0: return False
    return fookh(array, k, 0, len(array) - 1)

def fookh(array, k, start, end):
    if array[start] is k: return start
    if len(array) is 2 and array[1] is k: return 1
    
    mp = (end - start) // 2 + start
    if k <= array[mp]:
        return fookh(array, k, start, mp)
    else:
        return fookh(array, k, mp+1, end)

myArray = [0,1,1,2,2,3,3,3,4,4,4,4,4,4,5,5,5,5,5,6]
        #  0 1   3   5     8           14        19

print(firstOccurenceofK(myArray, 0))
print(firstOccurenceofK(myArray, 1))
print(firstOccurenceofK(myArray, 2))
print(firstOccurenceofK(myArray, 3))
print(firstOccurenceofK(myArray, 4))
print(firstOccurenceofK(myArray, 5))
print(firstOccurenceofK(myArray, 6))

def searchFirstOfK(array, k):
    left = 0
    right = len(array) - 1
    result = -1
    
    # array[left:right + 1] is the candidate set
    
    while left <= right:
        mid = left + ((right - left) // 2)
        if array[mid] > k:
            right = mid - 1
        else if array[mid] is k:
            result = mid
            # nothing to the right of mid can be the first occurrence of k
            right = mid - 1
        else:
            left = mid + 1
    return result