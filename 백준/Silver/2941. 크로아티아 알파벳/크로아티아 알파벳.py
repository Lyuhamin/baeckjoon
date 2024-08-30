croa = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
word = input().strip()

for c_al in croa:
    word = word.replace(c_al, "*")
   
print(len(word))
    