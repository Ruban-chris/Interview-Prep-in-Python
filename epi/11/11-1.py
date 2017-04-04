# Write a progra, that takes as input a set of sorted sequnces and computes the union
# of these sequences as a sorted sequence. 

class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
    def insert(self, k):
        self.heapList.append(k)
        self.currentSize = self.currentSize + 1
        self.percUp(self.currentSize)
    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc
    def minChild(self, i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i * 2 + 1
    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.percDown(1)
        return retval
    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while (i > 0):
            self.percDown(i)
            i = i - 1

#  = [0,0,3,5,6,6,7,28]
 
def mergeSortedLists(sortedLists):
    result = []
    minHeap = BinHeap()
    sortedListMaxLength = 0
    # for each sorted list add the smallest element into the heap
    
    for sortedList in sortedLists:
        sortedListMaxLength = max(sortedListMaxLength, len(sortedList))
        if len(sortedList) > 0:
            minHeap.insert(sortedList[0])
    j = 1

    while minHeap.currentSize is not 0 and j < sortedListMaxLength:
        for sortedList in sortedLists:
            if j < len(sortedList):
                minHeap.insert(sortedList[j])
                result.append(minHeap.delMin())
        j += 1

    while minHeap.currentSize is not 0:
        result.append(minHeap.delMin())

    return result

print(mergeSortedLists([[3,5,7],[0,6],[0,6,28]]))