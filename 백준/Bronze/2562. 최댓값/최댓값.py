num = [int(input().strip()) for i in range(9)]

max_val = max(num)

max_index = num.index(max_val) + 1

print(max_val)
print(max_index)