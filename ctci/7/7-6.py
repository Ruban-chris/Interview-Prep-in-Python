# NxN jigsaw puzzleself.design the data structures and explain the algorithms
# solve the puzzleself fitsWith

# assume that each puzzle piece can have at most 4 edges. and can fit with at most 4 pieces.
# puzzlePiece has edges, fitsWith, picture.

# piece
#    - solution. belongs to (x,y) of a particular puzzle. 
#    - fitsWith looks at the overall puzzle and determines if they are adjacent.

# Puzzle isSolved, tryPiece, shuffle, 

# a person gets all the pieces and shuffles them.
# then they sort the pieces by whether an edge is straight or not.
# they build a border.
# or they build a section.
# group by color
# or they use a reference. what the puzzle is supposed to look like. 

class Picture():
    def __init__(self, imageFile):
        self.jpeg
    gridPicture

class Puzzle():
    def __init__(self, n, picture):
        if n <= 1:
            raise Exception('The puzzle must have more than 1 piece')
        else:
            # divide up the picture into pieces
            
            self.placedPieces = []
        
        
    def size():
        
    
    
    placePiece():

class Piece():
    def __init__(self, picture, x, y):
        self.picture = picture
        self.x = None
        self.y = None
    def fitsWith(self, piece):
        return abs(self.x - piece.x) + abs(self.y - piece.y) == 1
    def assemble(self, piece):
    def numOfEdges(self):
        return 0
    # needs to rotate
        
        
# pieces can grow before they are placed into the puzzle into sub groupings.
    
    