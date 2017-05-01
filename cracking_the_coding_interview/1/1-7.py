# i didn't do this correctly
# Given an image represented by an NxN matrix, where each pixel in the image is 
# 4 bytes, write a method to rotate the image by 90 degrees.  Can you do this in place?

def rotateMatrix(matrix):
    rotatedMatrix = []
    rotatedRow = []
    for columnIndex in range(len(matrix[0])):
        for row in matrix:
            rotatedRow.append(row[columnIndex])
        rotatedMatrix.insert(0, rotatedRow)
        rotatedRow = []
    return rotatedMatrix

def rotateMatrixInPlace(matrix):
    k = 0
    i = 0
    j = 0
    n = len(matrix)
    copiedElement1 = None
    while k < n:
        if copiedElement1 is None:
            startPosition = [i, j]
            copiedElement1 = matrix[i][j]
        next_i = n - (j + 1)
        next_j = i
        nextPosition = [next_i, next_j]
        copiedElement2 = matrix[next_i][next_j]
        matrix[next_i][next_j] = copiedElement1
        copiedElement1 = copiedElement2
        if nextPosition == startPosition:
            copiedElement1 = None
            k += 1
            j = k
        else:
            i = next_i
            j = next_j
    return matrix

print(rotateMatrixInPlace([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]))

print(rotateMatrixInPlace([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))

print(rotateMatrixInPlace([
    [1, 2],
    [3, 4]
]))

# print(rotateMatrix([
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12],
#     [13, 14, 15, 16]
# ]))




# 
# 5 6
# 9 10
# 13 14 15
# 
# [
#     [4 8 12 16],
#     [3 7 11 15],
#     [2 6 10 14],
#     [1 5 9 13]
# ]
# 
# [
#     [3 6 9],
#     [2 5 8],
#     [1 4 7]
# ]
# 
# [
#     [1 2 3],
#     [4 5 6],
#     [7 8 9]
# ]
# 
# [
#     [3 6 9],
#     [2 5 8],
#     [1 4 7]
# ]
# 
# 
# for i in range(len(matrix)): 
#     rowToBeRotated = matrix[i]
#     
#     # grab all the elements in the row except the last one
#     
#     
#     