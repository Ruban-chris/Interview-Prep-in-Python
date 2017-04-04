import functools
import heapq
# heapq._heapify_max(listForTree)

def distance(point1, point2):
    return (
        (point2[0] - point1[0]) ** 2
        + (point2[1] - point1[1]) ** 2
        + (point2[2] - point1[2]) ** 2
        ) ** (1/2)
    
print(distance((0,0,0), (3,4,5)))



def findClosestKStars(k, file):
    maxHeap = new Queue.PriorityQueue(k + 1)
    
    star - 
    maxHeap.add(Star)
    
    if (maxHeap.size() == k + 1) {
        maxheap.remove()
    }
    Queue.PriorityQueue(k + 1)
    
# Given a class defining one ore more rich comparison ordering methods,
# this class decorate supplies the rest. 
# This simplifies the effort involved in specifying all of the possible rich comparison 
# operations. 

# The class must define one of __lt__(), __le__(), __gt__(), __ge__().  In addition
# the class should supply an __eq__()

@functools.total_ordering
class Star:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __eq__(self):
        return self.distance() is star.distance()
    def __lt__(self, star):
        return self.distance() < star.distance()
    def distance(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** (1/2)

