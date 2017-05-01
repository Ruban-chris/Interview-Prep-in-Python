def mergeSortedArrays(A1, A2):
    if len(A1) == 0: return A2
    if len(A2) == 0: return A1
    p1 = 0 
    p2 = 0
    while p1< len(A1) and p2 < len(A2):
        if A1[p1] < A2[p2]:
            p1 += 1
        else:
            A1.insert(p1, A2[p2])
            p1 += 1
            p2 += 1
    if p2 < len(A2):
        for i in range(p2, len(A2)):
            A1.append(A2[i])
    return A1

print(mergeSortedArrays([3,6], [2,4,20]))

