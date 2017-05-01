import time
import heapq
# stack api with heap

class Stack:
    def __init__(self, *args):
        if len(args) > 2: raise ValueException('expecting one array')
        if args and len(args) == 1:
            tuples = [(time.time(), x) for x in args[0]]
            self.heap = tuples
            heapq.heapify(self.heap)
        else:
            self.heap = []
    def push(self, obj):
        ts = time.time()
        negativeTS = -ts
        myTuple = (negativeTS, obj)
        heapq.heappush(self.heap, myTuple)
    def pop(self):
        ts = time.time()
        try:
            heapq.heappop(self.heap)
        except IndexError:
            print('no more elements to pop!')
    def peek(self):
        try:
            return self.heap[0][1]
        except IndexError:
            print('stack is empty')

    
    
myStack = Stack([4,5,6,8])
myStack.pop()
print('myStack', myStack.peek())
myStack.pop()
print('myStack', myStack.peek())
myStack.pop()
print('myStack', myStack.peek())
myStack.push(10)
print('myStack', myStack.peek())
myStack.pop()
myStack.pop()
myStack.pop()
myStack.peek()



