# search a maze

impossible_maze = [
    ['w','w','w','b','w'],
    ['w','w','w','b','b'],
    ['w','w','w','w','w'],
    ['w','w','w','w','w'],
    ['w','w','w','w','w']
]

maze = [
    ['w','w','w','w','w'],
    ['w','b','b','b','w'],
    ['b','w','w','w','w'],
    ['w','w','b','b','w'],
    ['w','w','b','w','w']
]

def searchMaze(array, start, end):
    path = []
    path.append(start)
    if searchMazeHelper(array, start, end, path):
        return path
    else:
        path.pop()
        return path

def isFeasible(position, array):
    if position[0] < 0 or position[0] >= len(array) or position[1] < 0 or position[1] >= len(array[0]) or array[position[0]][position[1]] == 'b':
        return False
    return True

def searchMazeHelper(array, current, end, path):
    if current[0] == end[0] and current[1] == end[1]:
        return True
    if array[current[0]][current[1]] is 'b':
        return False
    else:
        # color the current position so we don't backtrack
        array[current[0]][current[1]] = 'b'
        directions = [[-1, 0], [1,0], [0,1], [0, -1]]
        for direction in directions:
            next_pos = [current[0] + direction[0], current[1] + direction[1]]
            if isFeasible(next_pos, array):
                path.append(next_pos)
                if searchMazeHelper(array, next_pos, end, path):
                    return True
                path.pop()
        return False

assert(searchMaze(maze, [4,0], [0,4]) == [[4, 0], [3, 0], [3, 1], [2, 1], [2, 2], [2, 3], [2, 4], [1, 4], [0, 4]])
assert(searchMaze(impossible_maze, [4,0], [0,4]) == [])

# Time complexity is same as DFS O(v + e)
