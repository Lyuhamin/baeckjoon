s = int(input())
star = "*"
blank = " "


for i in range(1, s+1):
    print(blank * (s-i) + star * (i*2-1))

for j in range(s-1, 0, -1):
    print(blank * (s-j) + star * (j*2-1))