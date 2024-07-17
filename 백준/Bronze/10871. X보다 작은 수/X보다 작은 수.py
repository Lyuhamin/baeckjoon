N, X = map(int, input().strip().split())

numbers = list(map(int, input().strip().split()))

result = []

for number in numbers:
    if number < X:
        result.append(number)

print(' '.join(map(str, result)))