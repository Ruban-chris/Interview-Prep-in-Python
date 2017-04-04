# Given an M x N matrix in which each row and each column is sorted in 
# ascending order, write a method to find an element.

# first search by the first element in each row.

myMatrix = [
    [2, 4, 6, 8, 10],
    [12, 14, 16, 18, 20],
    [22, 24, 26, 28, 30],
    [32, 34, 36, 38, 40],
]

def searchMatrix(sortedMatrix, element):
    # guard case
    if len(sortedMatrix) is 0: return False
    row = len(sortedMatrix)//2
    col = len(sortedMatrix[0])//2
    return searchMatrixHelper(sortedMatrix, element, row, col)

def searchMatrixHelper(sortedMatrix, element, row, col):
    # guard case
    if row < 0 or col < 0: return False
    midPoint = (row, col)
    numOfColumns = len(sortedMatrix[0])
    numOfRows = len(sortedMatrix)
    soc = (0, col)
    sor = (row, 0)
    
    print('row', row)
    print('col', col)
    
    eor = (row, numOfColumns - 1)
    eoc = (numOfRows - 1, col)
    
    startOfColElement = sortedMatrix[soc[0]][soc[1]]
    startOfRowElement = sortedMatrix[sor[0]][sor[1]]
    endOfColElement = sortedMatrix[eoc[0]][eoc[1]]
    endOfRowElement = sortedMatrix[eor[0]][eor[1]]
    midPointElement = sortedMatrix[midPoint[0]][midPoint[1]]
    
    if element is midPointElement:
        return midPoint
    if element > midPointElement:
        if element > endOfRowElement:
            return searchMatrixHelper(sortedMatrix, element, row + 1, col)
        else:
            return searchMatrixHelper(sortedMatrix, element, row, col + 1)
        if element > endOfColElement:
            return searchMatrixHelper(sortedMatrix, element, row, col + 1)
        else:
            return searchMatrixHelper(sortedMatrix, element, row + 1, col)
    else:
        # element is less than mid Point element
        if element > startOfRowElement:
            return searchMatrixHelper(sortedMatrix, element, row, col - 1)
        else:
            return searchMatrixHelper(sortedMatrix, element, row-1, col)
            
        if element > startOfColElement:
            return searchMatrixHelper(sortedMatrix, element, row-1, col)
        else:
            return searchMatrixHelper(sortedMatrix, element, row, 0)

print(searchMatrix(myMatrix, 2))