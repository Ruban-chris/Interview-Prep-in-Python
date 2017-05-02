# paint a boolean matrix
import collections

Coordinate = collections.namedtuple('Coordinate', ('i', 'j'))
def paintMatrix(matrix, position):
    paintMatrixHelper(matrix, position, matrix[position.i][position.j])

def paintMatrixHelper(matrix, position, color):
    oobounds = position.i < 0 or position.j < 0 or position.i >= len(matrix) or position.j >= len(matrix[0])
    if oobounds: return
    colorAlreadyFlipped = matrix[position.i][position.j] != color
    if colorAlreadyFlipped: return
    else:
        matrix[position.i][position.j] = 'w' if color is 'b' else 'b'
        directions = [Coordinate(0,1), Coordinate(0, -1), Coordinate(1,0), Coordinate(-1, 0)]
        for direction in directions:
            paintMatrixHelper(matrix, Coordinate(direction.i + position.i, direction.j + position.j), color)

matrix1 = [
    ['b', 'w', 'b', 'w', 'w', 'w', 'b', 'b', 'b', 'b'],
    ['w', 'w', 'b', 'w', 'w', 'b', 'w', 'w', 'b', 'b'],
    ['b', 'b', 'b', 'w', 'w', 'b', 'b', 'w', 'b', 'b'],
    ['w', 'b', 'w', 'b', 'b', 'b', 'b', 'w', 'b', 'w'],
    ['b', 'w', 'b', 'w', 'w', 'w', 'w', 'b', 'w', 'w'],
    ['b', 'w', 'b', 'w', 'w', 'b', 'w', 'b', 'b', 'b'],
    ['w', 'w', 'w', 'w', 'b', 'w', 'b', 'w', 'w', 'b'],
    ['b', 'w', 'b', 'w', 'b', 'w', 'b', 'w', 'w', 'w'],
    ['b', 'w', 'b', 'b', 'w', 'w', 'w', 'b', 'b', 'b'],
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'b', 'b', 'w'],
]

matrix2 = [
    ['b', 'w', 'b', 'w', 'w', 'w', 'b', 'b', 'b', 'b'],
    ['w', 'w', 'b', 'w', 'w', 'b', 'w', 'w', 'b', 'b'],
    ['b', 'b', 'b', 'w', 'w', 'b', 'b', 'w', 'b', 'b'],
    ['w', 'b', 'w', 'b', 'b', 'b', 'b', 'w', 'b', 'w'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'w', 'w'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'w', 'w', 'b'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'w', 'w', 'w'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'],
    ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'b', 'w']
]

matrix3 = [
    ['b', 'w', 'w', 'w', 'w', 'w', 'b', 'b', 'b', 'b'],
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'b', 'b'],
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'b', 'b'],
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'b', 'w'],
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w'],
    ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
]

paintMatrix(matrix1, Coordinate(5, 4))
assert(matrix1 == matrix2)

paintMatrix(matrix2, Coordinate(3, 6))
assert(matrix2 == matrix3)
