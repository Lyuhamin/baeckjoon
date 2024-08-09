S = input().strip()

for char in range(ord('a'), ord('z') + 1):
    index = S.find(chr(char))
    print(index, end=' ')