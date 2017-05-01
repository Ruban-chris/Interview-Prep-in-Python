# Delete duplicates from sorted array
def deleteDuplicates(sortedArray):
    fillIndex = 0
    numValidElements = 0
    lastElement = None
    for i, element in enumerate(sortedArray):
        if element != lastElement:
            if lastElement != None:
                sortedArray[fillIndex] = element
            fillIndex += 1
            numValidElements += 1
            lastElement = element
    return numValidElements, sortedArray

def simple_test():
    actualNumValidElements, actualArray = deleteDuplicates([1,1,2,2,2,3])
    assert actualNumValidElements == 3
    assert actualArray == [1,2,3,2,2,3]

def main():
    simple_test()

if __name__ == '__main__':
    main()
