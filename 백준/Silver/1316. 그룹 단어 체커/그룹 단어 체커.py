N = int(input().strip())

word_count = 0

for _ in range(N):
    word = input().strip()
    previous_word = ''
    seen_word = set()
    t_f_word = True
    
    for char in word:
        if char != previous_word:
            if char in seen_word:
                t_f_word = False
                break
                
            seen_word.add(char)
        previous_word = char
        
    if t_f_word:
        word_count += 1
        
print(word_count)
        
            
                
    