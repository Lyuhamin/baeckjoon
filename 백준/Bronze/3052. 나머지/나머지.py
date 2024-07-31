remind = set()

for i in range(10):
    num = int(input().strip())
    rem = num % 42
    remind.add(rem)
    
print(len(remind))