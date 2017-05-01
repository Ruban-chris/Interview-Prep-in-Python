# You are given two sorted arrays, A and B. 
# where A has a large enough buffer at the end to hold Bself.
# Write a mthod to merge B int A in sorted order.

def mergeSortedArrays(A, B):
    # guard case
    if len(A) is 0: return B
    if len(B) is 0: return A
    
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        # compare the first element of A with the first element of B
        if (A[i] < B[j]):
            i += 1
        elif (A[i] >= B[j]):
            A.insert(i, B[j])
            i += 1
            j += 1
    if j < len(B):
        return A + B[j:]
    else:
        return A

A = [1,5,6,9,10]
B = [2,3,6,8]

print(mergeSortedArrays(A,B))