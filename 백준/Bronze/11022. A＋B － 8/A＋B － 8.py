T = int(input().strip())

for i in range(T):
    A, B = map(int, input().strip().split())
    print( "Case #{0}: {1} + {2} = {3}".format(i+1, A, B, A+B))