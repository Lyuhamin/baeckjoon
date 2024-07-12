T = int(input().strip())

for i in range(T):
    A, B = map(int, input().strip().split())
    print( "Case #{}: {} + {} = {}".format(i+1, A, B, A+B))