import sys


input = sys.stdin.readline
output = sys.stdout.write

T = int(input().strip())

for _ in range(T):
    A, B = map(int, input().strip().split())
    result = A + B
    output(f"{result}\n")
