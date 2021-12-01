def createMatrix(n,m):
    matrix = []
    for i in range(n):
        matrix.append([0]*m)
    return matrix

def printMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end=' ')
        print("")

def createIdentity(n):
    matrix = createMatrix(n, n)
    for i in range(n):
        matrix[i][i] = 1
    return matrix

def sumMatrixInternal(matrix):
    sum = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            sum += matrix[i][j]
    return sum

printMatrix(createIdentity(4))