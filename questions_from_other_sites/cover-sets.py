from collections import Counter
# for each index, find the smallest sub array that covers the set

paragraph = ['a', 'b', 'e', 'c', 'g', 'a', 'f', 'g', 'e', 'a', 'e']
set_to_cover = set(['a', 'g', 'e'])

def smallest_sub_array_covering_set(paragraph, set_to_cover):
    # counter is initialized with each word count at 1.
    # This can go negative or to a positive number greater than 1, depending on the
    # number of words encountered.
    words_to_cover_counter = Counter(set_to_cover)
    result = (-1, -1)
    num_of_uncovered_words = len(set_to_cover)
    left = 0
    for right, word in enumerate(paragraph):
        # if we encounter a word, we decrement the counter in words to cover
        if word in words_to_cover_counter:
            words_to_cover_counter[word] -= 1
            if words_to_cover_counter[word] == 0:
                num_of_uncovered_words -= 1

        while num_of_uncovered_words == 0:
            # set result if the difference of left and right is less than result
            if result == (-1, -1) or right - left < result[1] - result[0]:
                result = (left, right)

            leftWord = paragraph[left]
            if leftWord in words_to_cover_counter:
                words_to_cover_counter[leftWord] += 1
                if words_to_cover_counter[leftWord] == 1:
                    num_of_uncovered_words += 1
            left += 1
    return result

print('what', smallest_sub_array_covering_set(paragraph, set_to_cover))

class DoublyLinkedListNode:
    def __init__(self, data=None):
        self.data = data
        self.next = self.prev = None

class LinkedList:
    def __init__(self):
        self.head = self.tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def insert_after(self, value):
        node = DoublyLinkedListNode(value)
        node.prev = self.tail
        if self.tail:
            self.tail.next = node
        else:
            self.head = node
        self.tail = node
        self._size += 1

    def remove(self, node):
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        node.next = node.prev = None
        self._size -= 1
