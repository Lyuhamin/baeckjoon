w = int(input().strip())

for _ in range(w):
    word = input().strip()
    
    first_w = word[0]
    last_w = word[-1]
    
    print(first_w + last_w)