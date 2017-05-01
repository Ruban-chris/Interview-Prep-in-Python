# You have 3 towers and N disks of different sizes which can slide onto any tower.
# The puzzle starts with disks sorted in ascending order of size from top to bottom
# only one disc can be moved at a time.
# a disk is slid off the top of one tower onto another towers
# a disk cannot be placed on top of a smaller disck

# Write a program to move the disks from the first tower to the last using stacks

# base case and build approach

# start of array is base, end of array is top.

def moveDisks(n, originStack, destinationStack, bufferStack):
    # base case
    if n <= 0: return
    
    # move top n - 1 disks from origin to buffer, using destination as a buffer
    moveDisks(n - 1, originStack, bufferStack, destinationStack)
    
    # move top from origin to destinationStack
    moveTop(originStack, destinationStack)
    
    # move top n - 1 disks from buffer to destination, using origin as a buffer
    moveDisks(n - 1, originStack, bufferStack, destinationStack)
    
    