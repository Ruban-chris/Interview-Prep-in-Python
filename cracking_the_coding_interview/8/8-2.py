# count robot paths
# Imagine a robot sitting on the upper left corner of grid with r rows and c columns,
# The robot can only move in two directions, right and down, but certain cells are
# "off limits" such that the robot cannot step on them. Design an algorithm to find a
# path for the robot from the top left to the bottom right.

def countRobotPaths(grid):
    # guard case
    if len(grid) is 0: return 0
    if len(grid[0]) is 0: return 0

    r, c = len(grid), len(grid[0])
    memo = [[-1 for x in range(c)] for y in range(r)]
    # start at the end and work our way back towards the beginning
    return countRobotPathsHelper(grid, memo, (r - 1, c - 1))


def countRobotPathsHelper(grid, memo, position):
    r = position[0]
    c = position[1]
    if r < 0 or c < 0 : return 0
    if grid[r][c] is None: return 0
    if r is 0 and c is 0: return 1
    
    if memo[r][c] is -1:
        memo[r][c] = countRobotPathsHelper(grid, memo, (r - 1, c)) + countRobotPathsHelper(grid, memo, (r, c - 1))
    return memo[r][c]

grid = [
    [True, True, True, True],
    [None, True, True, True],
    [True, True, True, True],
    [True, True, True, True]
]

print(countRobotPaths(grid))
    