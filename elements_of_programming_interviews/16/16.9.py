from math import sqrt
from itertools import product
# implement a sudoku solver

my_board = [
    [0,2,0,0,0,0,0,0,0],
    [0,0,0,6,0,0,0,0,3],
    [0,7,4,0,8,0,0,0,0],
    [0,0,0,0,0,3,0,0,2],
    [0,8,0,0,4,0,0,1,0],
    [6,0,0,5,0,0,0,0,0],
    [0,0,0,0,1,0,7,8,0],
    [5,0,0,0,0,9,0,0,0],
    [0,0,0,0,0,0,0,4,0]
]

expected_board = [
  [1, 2, 6, 4, 3, 7, 9, 5, 8],
  [8, 9, 5, 6, 2, 1, 4, 7, 3],
  [3, 7, 4, 9, 8, 5, 1, 2, 6],
  [4, 5, 7, 1, 9, 3, 8, 6, 2],
  [9, 8, 3, 2, 4, 6, 5, 1, 7],
  [6, 1, 2, 5, 7, 8, 3, 9, 4],
  [2, 6, 9, 3, 1, 4, 7, 8, 5],
  [5, 4, 8, 7, 6, 9, 2, 3, 1],
  [7, 3, 1, 8, 5, 2, 6, 4, 9]
]

# i is my row
# j is my col

def sudoku_solver(partial_assignment):
    return sudoku_solver_helper(partial_assignment, 0, 0)

def sudoku_solver_helper(partial_assignment, i, j):
    if j == len(partial_assignment):
        # reset my col
        j = 0
        # move down a row
        i += 1
        if i == len(partial_assignment[0]):
            # base case, sudoku puzzle has been solved
            return True
    # skip spaces that have been filled
    if partial_assignment[i][j] != 0:
        return sudoku_solver_helper(partial_assignment, i, j + 1)
    else:
        for possible_entry in range(1,10):
            if is_new_entry_valid(partial_assignment, i, j, possible_entry):
                partial_assignment[i][j] = possible_entry
                if sudoku_solver_helper(partial_assignment, i, j + 1):
                    return True
                else:
                    partial_assignment[i][j] = 0

def is_new_entry_valid(partial_assignment, i, j, entry):
    # is the new entry already in the row?
    if entry in partial_assignment[i]:
        return False
    # is the new entry already in the column?
    if any(entry == partial_assignment[row_index][j] for row_index in range(0, 9)):
        return False
    # is the new entry in the sub grid?
    grid_size = int(sqrt(len(partial_assignment)))
    I = i//grid_size
    J = j//grid_size

    if any(entry == partial_assignment[I * grid_size + a][J * grid_size + b] for a,b in product(range(0,grid_size), repeat=2)):
        return False
    return True

sudoku_solver(my_board)
print(my_board)
