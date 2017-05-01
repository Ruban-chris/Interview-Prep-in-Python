def isPatternContainedInGrid(grid, pattern):
    # Each entry in previousAttempts is a point in the grid and suffix of pattern
    # identified by its offset.  Presence in previousAttempts
    # indiciates the suffix is not contained in the grid starting from that point.
    
    previousAttempts = set()
    
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (isPatternSuffixContainedStartingAtXY(grid, i, j, pattern, 0, previousAttempts)):
                return True
    
    return False

def isPatternSuffixContainedStartingAtXY(grid, x, y, pattern, offset, previousAttempts):
    if len(pattern) == offset:
        return True
    
    # check if (x,y) lies within grid
    if (x < 0 or x >= len(grid)) or y < 0 or y >= len(grid[x]) or (x,y,offset) in previousAttempts:
        return False
    
    if grid[x][y] == pattern[offset] and (isPatternSuffixContainedStartingAtXY(grid, x - 1, y, pattern, offset + 1, previousAttempts) or
                                          isPatternSuffixContainedStartingAtXY(grid, x + 1, y, pattern, offset + 1, previousAttempts) or
                                          isPatternSuffixContainedStartingAtXY(grid, x, y - 1, pattern, offset + 1, previousAttempts) or
                                          isPatternSuffixContainedStartingAtXY(grid, x, y + 1, pattern, offset + 1, previousAttempts)
                                          ):
        return True
    previousAttempts.add((x,y,offset))
    return False