import math

def create_identity(n):
    identity = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        identity[i][i] = 1
    return identity

def matrix_divide(matrix, n):
    return [[matrix[i][j] / n for j in range(len(matrix[0]))] for i in range(len(matrix))]

def matrix_sum(matrix, matrix2):
    return [[matrix[i][j] + matrix2[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]

def matrix_sub(matrix, matrix2):
    return [[matrix[i][j] - matrix2[i][j] for j in range(len(matrix[0]))] for i in range(len(matrix))]

def mat_mul(matrix, matrix2):
    return [[sum(matrix[i][k] * matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))] for i in range(len(matrix))]

def exp(matrix):
    new_term, result = create_identity(len(matrix)), create_identity(len(matrix))
    precision, k = 1.0, 1.0
    while precision >= 0.001:
        new_term = mat_mul(new_term, matrix)
        new_term = matrix_divide(new_term, k)
        result = matrix_sum(new_term, result)
        precision = sum(abs(x) for line in new_term for x in line)
        k += 1
    return result

def cos(matrix):
    new_term, result = create_identity(len(matrix)), create_identity(len(matrix))
    precision, k = 1.0, 1
    while precision >= 0.001:
        for _ in range(2):
            new_term = mat_mul(new_term, matrix)
        new_term = matrix_divide(new_term, k * 2 * (k * 2 - 1))
        if k % 2 == 0:
            result = matrix_sum(result, new_term)
            precision = sum(abs(x) for line in new_term for x in line)
        else:
            result = matrix_sub(result, new_term)
        k += 1
    return result

def sin(matrix):
    new_term, result = create_identity(len(matrix)), create_identity(len(matrix))
    precision, k = 1.0, 1
    while precision >= 0.001:
        for _ in range(2):
            new_term = mat_mul(new_term, matrix)
        new_term = matrix_divide(new_term, k * 2 * (k * 2 - 1))
        if k % 2 == 1:
            result = matrix_sub(result, new_term)
            precision = sum(abs(x) for line in new_term for x in line)
        else:
            result = matrix_sum(result, new_term)
        k += 1
    return result

def cosh(matrix):
    new_term, result = create_identity(len(matrix)), create_identity(len(matrix))
    precision, k = 1.0, 1
    while precision >= 0.001:
        for _ in range(2):
            new_term = mat_mul(new_term, matrix)
        new_term = matrix_divide(new_term, k * 2 * (k * 2 - 1))
        if k % 2 == 0:
            result = matrix_sum(result, new_term)
            precision = sum(abs(x) for line in new_term for x in line)
        else:
            result = matrix_sub(result, new_term)
        k += 1
    return result

def sinh(matrix):
    new_term, result = create_identity(len(matrix)), create_identity(len(matrix))
    precision, k = 1.0, 1
    while precision >= 0.001:
        for _ in range(2 + 1):
            new_term = mat_mul(new_term, matrix)
        new_term = matrix_divide(new_term, k * 2 * (k * 2 - 1) + 1)
        if k % 2 == 1:
            result = matrix_sum(result, new_term)
        else:
            precision = sum(abs(x) for line in new_term for x in line)
        k += 1
    return result

def trigo(function, matrix):
    if (function == "COS"):
        matrix = cos(matrix)
    elif (function == "SIN"):
        matrix = sin(matrix)
    elif (function == "COSH"):
        matrix = cosh(matrix)
    elif (function == "SINH"):
        matrix = sinh(matrix)
    elif (function == "EXP"):
        matrix = exp(matrix)
    print('\n'.join("\t".join(f"{x:.2f}" if x != 0 else "0.00" for x in line) for line in matrix))
    return 0
