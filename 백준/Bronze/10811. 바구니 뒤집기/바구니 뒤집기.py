N, M = map(int, input().split())

B = list(range(1, N + 1))

for _ in range(M):
    i, j = map(int, input().split())
    B[i-1:j] = B[i-1:j][::-1]
    
print(' '.join(map(str, B)))