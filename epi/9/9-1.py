# astack with max
# stack with push pop and max

class Stack:
    def __init__(self):
        self.data = []
        self.max = []
    def push(self, value):
        if len(self.max) is 0:
            self.max.append(value)
            self.data.append(value)
            return

        lastMax = self.max[len(self.max) - 1]
        if value > lastMax:
            self.max.append(value)
        else:
            self.max.append(lastMax)
        self.data.append(value)
    def pop(self):
        self.max.pop()
        return self.data.pop()
    def getMax(self):
        print('self.max', self.max)
        print('self.data', self.data)
        if len(self.max) is 0:
            return None
        lastMax = self.max[len(self.max) - 1]
        return lastMax

myStack = Stack()

myStack.push(1)
print(myStack.getMax())
myStack.push(2)
print(myStack.getMax())
myStack.push(8)
print(myStack.getMax())
myStack.push(6)
print(myStack.getMax())
myStack.push(10)
print(myStack.getMax())
myStack.push(15)
print(myStack.getMax())
myStack.push(20)
print(myStack.getMax())
myStack.push(3)
print(myStack.getMax())

myStack.pop()
print(myStack.getMax())
myStack.pop()
print(myStack.getMax())
myStack.pop()
print(myStack.getMax())
myStack.pop()
print(myStack.getMax())
myStack.pop()
print(myStack.getMax())

myStack.pop()
print(myStack.getMax())
myStack.pop()
print(myStack.getMax())

myStack.pop()
print(myStack.getMax())




