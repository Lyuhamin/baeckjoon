mat = []

for i in range(9):
    row = list(map(int, input().split()))
    mat.append(row)
    
max_val = -1
max_row, max_col = 0, 0

for j in range(9):
    for k in range(9):
        if mat[j][k] > max_val:
            max_val = mat[j][k]
            max_row, max_col = j + 1, k + 1
            
print(max_val)
print(max_row, max_col)
        
    