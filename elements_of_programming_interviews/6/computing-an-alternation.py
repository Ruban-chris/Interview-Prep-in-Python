import random

# This method first sorts the array then does a pairwise swap
# Time complexity is O(nlogn)
# Space complexity is constant
def alternate_array(A):
    if len(A) < 2: return A
    A.sort()
    for i in range(1, len(A), 2):
        if i + 1 <= len(A) - 1:
            A[i], A[i + 1] = A[i + 1], A[i]

# The EPI solution is better in time complexity
# It goes down the array and reverses two elements if i is odd,
# otherwise it leaves it alone
# Time complexity is O(n)
# Following is from EPI solutions

def rearrange(A):
    for i in range(len(A)):
        A[i:i+2] = sorted(A[i:i+2], reverse=i%2)

def check_answer(A):
    for i in range(len(A)):
        if i % 2:
            assert A[i] >= A[i - 1]
            if i + 1 < len(A):
                assert A[i] >= A[i + 1]
        else:
            if i > 0:
                assert A[i - 1] >= A[i]
            if i + 1 < len(A):
                assert A[i + 1] >= A[i]

for _ in range(10000):
    n = random.randint(1, 10)
    A = [random.randint(-n, n) for _ in range(n)]
    alternate_array(A)
    check_answer(A)
