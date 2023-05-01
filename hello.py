def matrix_mult(a, b):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
    return result

def matrix_pow(matrix, n):
    if n == 1:
        return matrix
    elif n % 2 == 0:
        half_pow = matrix_pow(matrix, n // 2)
        return matrix_mult(half_pow, half_pow)
    else:
        return matrix_mult(matrix, matrix_pow(matrix, n - 1))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        matrix = [[1, 1], [1, 0]]
        return matrix_pow(matrix, n - 1)[0][0]

# prints the most epic user 
print('moomoo02')

#prints the least epic user
print('DevLuke')

for i in range(10):
    print(fibonacci(i))