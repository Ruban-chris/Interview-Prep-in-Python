# implement the "paint fill" function that one might see on many image editing
# programs. That is, given a screen (represented by a two-dimensional array of colors)
# a point and a new color, fill in the surrounding area until the color changes from the 
# original color.

def paintFill(screen, point, color):
    r = point[0]
    c = point[1]
    originalColor = screen[r][c]
    screen[r][c] = color
    
    print('r',r)
    print('c',c)
    
    
    if r + 1 < len(screen):
        if screen[r + 1][c] is originalColor:
            paintFill(screen, (r + 1, c), color)
    
    if c + 1 < len(screen[r]):
        if screen[r][c + 1] is originalColor:
            paintFill(screen, (r, c + 1), color)
    
    if c - 1 >= 0:
        if screen[r][c - 1] is originalColor:
            paintFill(screen, (r, c -1), color)

    if r - 1 >= 0:
        if screen[r - 1][c] is originalColor:
            paintFill(screen, (r - 1, c), color)

screen = [
    ['g','r','r','r'],
    ['r','r','g','g'],
    ['r','g','g','g']
]

paintFill(screen, [2,2], 'b')
print('screen', screen)