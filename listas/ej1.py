def suma_lista(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma

lista = [1,2,3,4]

print(suma_lista(lista))
print(sum(lista))