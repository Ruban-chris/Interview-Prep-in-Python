def waysToClimb(k,n):
    memo = [-1] * (n + 1)
    return wtch(k,n,memo)

def wtch(k,n,memo):
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 1
    if memo[n] is -1:
        for i in range(1, k+1):
            memo[n] += wtch(k, n - i, memo)
    else: 
        return memo[n]

print(waysToClimb(2,4))