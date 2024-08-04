N = int(input())
M = list(map(int, input().split()))

max_M = max(M)

new_M = [(i / max_M) * 100 for i in M]
new_average = sum(new_M) / N

print(new_average)
