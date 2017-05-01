# search in 2d array where rows and cols are non decreasing

myarray = [
    [-1, 2, 4, 4, 6],
    [1, 5, 5, 9, 21],
    [3, 6, 6, 9, 22],
    [3, 6, 8, 10, 24],
    [6, 8, 9, 12, 25],
    [8, 10, 12, 13, 40],
]

def search2d(array, el):
    colRange = [0, len(array[0]) - 1]
    for row in array:
        if el >= row[colRange[0]] and el <= row[colRange[1]]:
            for columnIndex in range(colRange[0], colRange[1] + 1):
                if el == row[columnIndex]:
                    return True
                if el < row[columnIndex]:
                    colRange[1] = columnIndex - 1
                    break
                
    return False
    
print(search2d(myarray, 7))

def matrixSearch(A, x):
    row = 0
    col = len(A[0]) - 1
    while row < len(A) and col >= 0:
        if A[row][col] == x:
            return True
        else if A[row][col] < x:
            row += 1
        else:
            col -= 1
    return False

# O(m + n)
    