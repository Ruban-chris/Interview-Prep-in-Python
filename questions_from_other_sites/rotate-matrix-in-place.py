# rotate a n x n matrix 90 degrees clockwise

def rotate(matrix):
    n = len(matrix)
    for i in range(0, n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = temp
    return matrix

def rotateMatrixNinetyDegreesClockwise(matrix):
    start = 0
    n = len(matrix[0])
    end = n - 1
    while start < end:
        for i in range(start, end):
            # do 4 loops
            position = [start,i]
            element = matrix[position[0]][position[1]]
            for _ in range(0,4):
                nextPosition = [position[1], n - position[0] - 1]
                temp = matrix[nextPosition[0]][nextPosition[1]]
                matrix[nextPosition[0]][nextPosition[1]] = element
                position = nextPosition
                element = temp

        start += 1
        end -=1
    return matrix

print(rotateMatrixNinetyDegreesClockwise([[1,2],[3,4]]))
