import collections
Number_with_range_diff = collections.namedtuple('Number_with_range_diff', ('numbers', 'range_difference'))

def find_minimum_range_elements(A1, A2, A3):
    p1, p2, p3 = 0, 0, 0
    numbersWithRangeDiff = Number_with_range_diff([], float('inf'))
    while p1 <= len(A1) - 1 and p2 <= len(A2) - 1 and p3 <= len(A3) - 1:
        minEl = min(A1[p1], A2[p2], A3[p3])
        maxEl = max(A1[p1], A2[p2], A3[p3])
        range_difference = abs(maxEl - minEl)

        if range_difference < numbersWithRangeDiff.range_difference:
            numbersWithRangeDiff = Number_with_range_diff([A1[p1], A2[p2], A3[p3]], range_difference)

        if A1[p1] <= A2[p2] and A1[p1] <= A3[p3]:
            p1 += 1
        elif A2[p2] <= A1[p1] and A2[p2] <= A3[p3]:
            p2 += 1
        elif A3[p3] <= A2[p2] and A3[p3] <= A1[p1]:
            p3 += 1

    return numbersWithRangeDiff.numbers


# Test Cases
assert([15,15,16] == find_minimum_range_elements([5,10,15], [3,6,9,12,15], [8,16,24]))
assert([4,4,4] == find_minimum_range_elements([1,2,3,4], [4,5,6,7], [-1,0,2,3,4]))
assert([0,0,0] == find_minimum_range_elements([0],[0],[0]))

# Complexity
# T O(n)
# S O(1)
