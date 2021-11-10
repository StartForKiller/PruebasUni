import numpy as np

def posOfMax(vector) -> np.double:
    maxValue = 0
    pos = 0
    for i in range(0, vector.size):
        if vector[i] > maxValue:
            pos = i
            maxValue = vector[i]
    return pos

def posOfMin(vector) -> np.double:
    minValue = posOfMax(vector)
    pos = -1
    for i in range(0, vector.size):
        if vector[i] < minValue:
            pos = i
            minValue = vector[i]
    return pos

n = int(input("Dame el tamaño del vector: "))

rng = np.random.default_rng()

array1 = np.zeros((n,n), np.double)

array1[:] = rng.random(n*n, np.double).reshape((n,n))

print("El vector 1 es:\n {}".format(array1))

for i in range(0, n):
    columna = array1[:,i]
    maxPos = posOfMax(columna)
    minPos = posOfMin(array1[maxPos])
    if(minPos == i):
        print("Tenemos un punto de silla en la columna {} y fila {}: {}".format(minPos, maxPos, array1[:,i][minPos]))
