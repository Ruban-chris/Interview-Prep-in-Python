maze = [
    ["start", "white", "white", "black", "white"],
    ["white", "black", "white", "black", "white"],
    ["black", "white", "white", "black", "white"],
    ["white", "white", "black", "white", "white"],
    ["black", "white", "white", "black", "white"],
    ["white", "black", "white", "white", "end"]
]

def findPath(maze, start, end):
    path = []
    path.append(start)
    maze[start[0]][start[1]] = "Black"
    if findPathHelper:
        return path
    else:
        path.pop()
        return path

def findPathHelper(maze, current, path):
    if maze[current[0][current[1]] is 'end':
        return True
    
    directions = [(0,1),(1,0),(-1,0),(0,-1)]
    
    for direction in directions:
        nextPosition = (current[0] + direction[0], current[1] + direction[1])
        if isFeasible(maze, nextPosition):
            path.append(nextPosition)
            if (findPathHelper(maze, nextPosition, path):
                return True
            path.pop()
    return False
        

def isFeasible(maze, position):
    if position[0] < 0 or position[1] < 0 or position[0] >= len(maze) or position[1] >= len(maze[0])
        return False
    else:
        return True