def zeroOutCol(matrix, j):
    for i in range(len(matrix)):
        matrix[i][j] = 0
    return matrix

def zeroOutRow(matrix, i):
    for j in range(len(matrix[0])):
        matrix[i][j] = 0
    return matrix

def createBitVector(length, val):
    bv = []
    for i in range(length):
        bv.append(val)
    return bv

def zeroMatrix(matrix):
    rowBv = createBitVector(len(matrix), 1)
    colBv = createBitVector(len(matrix[0]), 1)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            el = matrix[i][j]
            if el is 0:
                rowBv[i] = 0
                colBv[j] = 0
    print('rowBv', rowBv)
    print('colBv', colBv)
    for i in range(len(rowBv)):
        if rowBv[i] is 0:
            zeroOutRow(matrix, i)
    for j in range(len(colBv)):
        if colBv[j] is 0:
            zeroOutCol(matrix, j)
    return matrix

print(zeroMatrix([
    [1, 2, 3, 0],
    [5, 6, 7, 8],
    [0, 10, 11, 12]
    ]
))