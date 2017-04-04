# Sparse search
# Given a sorted array of strings that is interspersed with empty strings 
# write a method to find the location of a given string

mySparseArray = ["abc", "", "", "", "bagr", "", "", "", "", "cef"]

def search(strings, stringToFind, first, last):
    if first > last: return -1
    
    # move mid to the middle
    mid = (last + first)//2
    
    # if mid is empty, find the closest non-empty string
    if strings[mid] is "":
        left = mid - 1
        right = mid + 1
        while True:
            if left < first && right > last:
                return -1
            elif right <= last and strings[right] is not "":
                mid = right
                break
            elif left >= first and string[left] is not "":
                mid = left
                break
            right++
            left++
    if stringToFind is strings[mid]:
        return mid
    elif strings[mid] < stringToFind:
        return search(strings, stringToFind, mid + 1, last)
    else:
        return search(strings, stringToFind, first, mid - 1)
            
    
        