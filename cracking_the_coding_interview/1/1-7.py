def rotate_matrix(square_matrix):
    length = len(square_matrix)
    for i in range(length//2):
        for j in range(i, length - i - 1):
            k = j
            l = (length - i - 1)
            m = l
            n = (length - k - 1)
            o = n
            p = (length - l - 1)
            (square_matrix[i][j],
            square_matrix[k][l],
            square_matrix[m][n],
            square_matrix[o][p]) = (square_matrix[o][p],
                square_matrix[i][j],
                square_matrix[k][l],
                square_matrix[m][n])

square_1 = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]
rotate_matrix(square_1)
print(square_1)

[
    [7, 11, 5, 15],
    [14, 12, 16, 10],
    [9, 3, 1, 2],
    [13, 4, 8, 6]
]
