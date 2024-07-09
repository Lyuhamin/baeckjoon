X = int(input())
N = int(input())

calcul = 0

for i in range(N):
    a, b = map(int, input().split())
    calcul += a * b
    
if calcul == X:
    print("Yes")
else:
    print("No")