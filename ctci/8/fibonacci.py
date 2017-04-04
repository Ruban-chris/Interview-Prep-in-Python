import traceback
# is python normal order vs applicative order
# fully expand then reduce or evaluate arguments then apply.
# in python maximum recursion is 1000.

# simple recursive
def fibonacci(i):
    if i == 0:
        return 0
    if i == 1:
        return 1
    return fibonacci(i - 1) + fibonacci(i - 2)
    
# print(fibonacci(36))

# memoization or top down dynamic programming

def memo_fibonacci(n):
    return fibonacciHelper(n, [0] * (n + 1))

def fibonacciHelper(i, memo):
    print('fib called', i, memo)
    if i == 0 or i == 1:
        print('base case')
        memo[i] = i
        return i
    if memo[i] == 0:
        print('did not have it')
        memo[i] = fibonacciHelper(i - 1, memo) + fibonacciHelper(i - 2, memo)
    print('memoized', i, 'value', memo[i])
    return memo[i]

# print(memo_fibonacci(4))

# bottom up dynamic programming 

def bottom_up_fibonacci(n):
    # guard case
    if (n == 0): return 0
    elif (n == 1): return 1

    memo = [0] * n
    memo[0] = 0
    memo[1] = 1
    for i in range(2, n):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n-1] + memo[n - 2]

print(bottom_up_fibonacci(36))

# more efficient bottom up dynamic programming without array
def bottom_up_efficient_fibonacci(n):
    if n == 0: return 0
    a = 0
    b = 1
    for i in range(2, n):
        c = a + b
        a = b
        b = c
    return a + b

print(bottom_up_efficient_fibonacci(36))
    