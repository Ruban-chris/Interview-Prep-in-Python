# reverse the words in a string

def reverse(array, start, end):
    p1 = start
    p2 = end
    print('p1', p1)
    print('p2', p2)
    while p1 < p2:
        temp = array[p1]
        array[p1] = array[p2]
        array[p2] = temp
        p1 += 1
        p2 -= 1
    return array
    
def find(array, char, start):
    for i in range(start, len(array)):
        if (array[i] is char):
            return i
    return -1

find(['B', 'o', 'b', ' ', 'l', 'i', 'k', 'e', 's', ' ', 'A', 'l', 'i', 'c', 'e'], ' ', 10)

def reverseWords(array):
    reversedArray = reverse(array, 0, len(array) - 1)
    start = 0
    end = find(array, ' ', start)
    # go through the reversed array, looking for each word and reversing it.
    while end != -1:
        reverse(array, start, end)
        start = end + 1
        end = find(array, ' ', start)
        print(array[end])
        
    
    reverse(array, start, len(array))
    return array
    
print(reverseWords(['B', 'o', 'b', ' ', 'l', 'i', 'k', 'e', 's', ' ', 'A', 'l', 'i', 'c', 'e']))