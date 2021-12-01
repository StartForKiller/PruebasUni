def potencia(lista, n):
    suma = 0
    for x in lista:
        suma += x**n
    return suma

lista = [1,2,3,4]

print(potencia(lista, 2))