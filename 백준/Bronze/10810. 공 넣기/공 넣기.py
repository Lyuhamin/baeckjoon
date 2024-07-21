N, M = map(int, input().split())

B = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    for index in range(i - 1, j):
        B[index] = k
        
print(' '.join(map(str, B)))
        

