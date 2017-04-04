import time
# given quarters, dimes, and nickels and pennies, write code
# to calculate the numer of ways of representing n cents.

# naive recursive method
def numberOfWaysToMakeChange(n):
    if n is 0:
        return 1
    if n < 0:
        return 0
    else:
        return numberOfWaysToMakeChange(n - 25) + numberOfWaysToMakeChange(n - 10) + numberOfWaysToMakeChange(n - 5) + numberOfWaysToMakeChange(n - 1)

# t0 = time.time()
# print(numberOfWaysToMakeChange(50))
# t1 = time.time()
# total1 = t1-t0
# print('total1', total1)


# memoized method
def memoNumberOfWaysToMakeChange(n):
    # guard case
    if n is 0: return 0
    memo = {}
    return memoNumberOfWaysToMakeChangeHelper(n, memo)
    
def memoNumberOfWaysToMakeChangeHelper(n, memo):
    # base case
    if n > 0:
        if n in memo:
            return memo[n]
        else:
            memo[n] = memoNumberOfWaysToMakeChangeHelper(n - 25, memo) + memoNumberOfWaysToMakeChangeHelper(n - 10, memo) + memoNumberOfWaysToMakeChangeHelper(n - 5, memo) + memoNumberOfWaysToMakeChangeHelper(n - 1, memo)
    if n is 0:
        return 1
    elif n < 0:
        return 0

    return memo[n]

t2 = time.time()
print(memoNumberOfWaysToMakeChange(10))
t3 = time.time()
total2 = t3 - t2
print('total2', total2)
