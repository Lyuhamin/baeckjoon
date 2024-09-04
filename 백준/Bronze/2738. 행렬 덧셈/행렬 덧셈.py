def read_matrix(n, m):
    matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    return matrix

def add_matrices(matrix_a, matrix_b, n, m):
    result = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    return result

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


N, M = map(int, input().split())

A = read_matrix(N, M)
B = read_matrix(N, M)
result = add_matrices(A, B, N, M)

print_matrix(result)
