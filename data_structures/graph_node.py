class GraphNode:
    def __init__(self, initdata):
        self.data = initdata
        self.adjacent = []
    def getData(self):
        return self.data
    def setData(self, newData):
        self.data = newData
    def insertLeft(self, node):
        self.adjacent.insert(0)
    def insertRight(self, node):
        self.adjacent.append(x)
    def removeRight(self):
        self.adjacent.pop[len(self.adjacent) - 1]
    def removeLeft(self):
        self.adjacent.pop[0]