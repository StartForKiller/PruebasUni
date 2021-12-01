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

def createIdentity(n,m):
    matrix = createMatrix(n, m)
    for i in range(min(n, m)):
        matrix[i][i] = 1
    return matrix

printMatrix(createIdentity(4,4))