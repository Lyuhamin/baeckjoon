c = [1, 1, 2, 2, 2, 8]

n = list(map(int, input().split()))

list_last = [c[i] - n[i] for i in range(6)]

print(" ".join(map(str, list_last)))