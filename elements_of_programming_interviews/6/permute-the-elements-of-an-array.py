# This solution swaps elements in both A and P until P is sorted.
# Time complexity is O(n)
# Uses no additional space
def apply_permutation(A, P):
    i = 0
    while i <= len(A) - 1:
        temp = P[i]
        if temp != i:
            # each time we are moving one element to the correct position.
            A[i], A[temp] = A[temp], A[i]
            P[i], P[temp] = P[temp], P[i]
        else:
            i+=1
    return A

my_array = ['a','b','c','d','e']
assert ['d', 'c', 'b', 'e', 'a'] == apply_permutation(my_array, [4,2,1,0,3])
