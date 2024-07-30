all_stu = set(range(1, 31))

sub_stu = set()
for _ in range(28):
    sub_stu.add(int(input().strip()))
    
miss_stu = sorted(all_stu - sub_stu)

print(miss_stu[0])
print(miss_stu[1])