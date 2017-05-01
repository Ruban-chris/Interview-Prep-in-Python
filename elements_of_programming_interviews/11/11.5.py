from heapq import heappush, heappop
global_result = []
def median(sequence):
    minHeap = []
    maxHeap = []

    for element in sequence:
        heappush(minHeap, element)
        if len(minHeap) - len(maxHeap) > 1:
            heappush(maxHeap, -heappop(minHeap))

        if (len(minHeap) + len(maxHeap)) % 2 is 0:
            minHeapPeek = minHeap[0]
            maxHeapPeek = -maxHeap[0]
            global_result.append((minHeapPeek + maxHeapPeek) / 2)
        else:
            global_result.append(minHeap[0])

# print(median([1,0,3,5,2,0,1]))

def simple_test():
    stream = [1, 2, 3, 4, 5]
    median(iter(stream))
    assert global_result == [1, 1.5, 2, 2.5, 3]

def main():
    simple_test()

if __name__ == '__main__':
    main()
