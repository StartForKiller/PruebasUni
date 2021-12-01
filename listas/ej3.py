def por_ceros(lista):
    count = 0
    for i in range(len(lista)):
        if lista[i] < 0:
            lista[i] = 0
            count += 1
    return count

lista = [1,-1,3,4]

print(por_ceros(lista))
print(lista)