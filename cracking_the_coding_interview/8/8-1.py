# A child is running up a staircase with n steps and can hop either 1 step, 2 step,
# or 3 steps. count how many ways the child can run up the stairs.
def countPathsUpStairs(n):
    return countPathsUpStairsHelper(n, [0] * (n + 1))


def countPathsUpStairsHelper(n, memo):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    elif memo[n] == 0:
        memo[n] = countPathsUpStairsHelper(n - 1, memo) + countPathsUpStairsHelper(n - 2, memo) + countPathsUpStairsHelper(n - 3, memo)
    return memo[n]

print(countPathsUpStairs(50))