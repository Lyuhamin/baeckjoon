words = []
for i in range(5):
    word = input()
    words.append(word)
  
max_len = max(len(word) for word in words)

result = ''

for j in range(max_len):
    for word in words:
        if j < len(word):
            result += word[j]
            
print(result) 

