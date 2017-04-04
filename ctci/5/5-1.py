def insertion2(N, M, i, j):
    return (M << i) | (N & ( (~0 << (j + 1)) | ((1 << i) - 1)))
    
N = int('10111000000', 2)
M = int('11001', 2)
i = 3
j = 7

print(bin(insertion2(N, M, i, j)))