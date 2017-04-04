from operator import itemgetter
from copy import copy
# You have a boxStack of n boxes, with widths wi, heights hi, and depths di.
# The boxes cannot be rotated and can only be boxStacked on top of one another
# if each box in the stack is stricktly larger than the box above it in width, height, and depth.
# Implement a method to compute the height of the tallest possible stack.
# The height of a stack is the sum of the heights of each box. 
# (w,h,d)
# stack is an array where the top is the end.

def tallestStack(boxes):
    # sort the boxes by any dimensions.  Here we're sorting by height
    boxesSortedByWidthDescending = sorted(boxes, key=itemgetter(1), reverse=True)
    return boxStackHeight(tallestStackHelper(boxesSortedByWidthDescending, []))

def tallestStackHelper(sortedBoxes, boxStack):
    if len(sortedBoxes) is 0:
        return boxStack
    else:
        
        sortedBoxesWithoutFirstBox = copy(sortedBoxes)
        sortedBoxesWithoutFirstBox.pop(0)
        boxToStack = copy(sortedBoxes[0])
        print('boxStack', boxStack)
        if boxCanBeStacked(boxStack, boxToStack):
            boxStackWithFirstBox = copy(boxStack)
            boxStackWithFirstBox.append(boxToStack)
        else:
            boxStackWithFirstBox = copy(boxStack)
        
        return max(tallestStackHelper(sortedBoxesWithoutFirstBox, boxStackWithFirstBox), tallestStackHelper(sortedBoxesWithoutFirstBox, boxStack))
        
        
        
        
    

def boxCanBeStacked(boxStack, upperBox):
    if len(boxStack) is 0:
        return True
    else:
        topOfStack = boxStack[len(boxStack) - 1]
        if topOfStack[0] > upperBox[0] and topOfStack[1] > upperBox[1] and topOfStack[2] > upperBox[2]:
            return True
    return False
    
def boxStackHeight(boxStack):
    height = 0
    for box in boxStack:
        height += box[1]
    return height
    
boxes = [(1,1,1),(2,1,1),(2,2,1),(2,2,2),(3,2,2),(3,3,2),(3,3,3),(4,3,3),(4,4,3),(4,4,4)]

print(tallestStack(boxes))

# books solution

def createStack(boxes):
    sorted(boxes, key=itemgetter[1], reverse=True)
    memo = [-1] * (len(boxes) + 1)
    return createStackHelper(boxes, null, 0, memo)

def createStackHelper(boxes, bottom, offset, memo):
    if offset >= len(boxes): return 0 # base case
    
    newBottom = boxes[offset]
    heightWithBottom = 0
    if bottom is None or newBottom.canBeAbove(bottom):
        if memo[offset] is 0:
            memo[offset] = createStack(boxes, newBottom, offset + 1, memo)
            memo[offset] += newBottom.height
        heightWithBottom = memo[offset]
    
    heightWithoutBottom = createStack(boxes, bottom, offfset + 1, memo)
    
    return max(heightWithBottom, heightWithOutBottom)