def check_equals(m1, m2):
    for l1, l2 in m1, m2:
        for i1, i2 in l1, l2:
            if (i1 != i2):
                return 84
    return 0

def exp(matrix):
    
    return 0

def cos(matrix):
    
    return 0

def sin(matrix):
    return 0

def cosh(matrix):
    return 0

def sinh(matrix):
    return 0

def mat_mul(matrix, matrix2):
    return [[sum(matrix[i][k] * matrix2[k][j] for k in range(len(matrix2))) for j in range(len(matrix2[0]))] for i in range(len(matrix))]

def trigo(function, matrix):
    if (function == "COS"):
        cos(matrix)
    elif (function == "SIN"):
        sin(matrix)
    elif (function == "COSH"):
        cosh(matrix)
    elif (function == "SINH"):
        sinh(matrix)
    elif (function == "EXP"):
        exp(matrix)
    print('\n'.join("\t".join(f"{x:.2f}" if x != 0 else "0.00" for x in line) for line in matrix))
    return 0
