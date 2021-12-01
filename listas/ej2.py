def max_idx(lista):
    max = 0
    maxI = -1
    for i in range(len(lista)):
        valor = lista[i]
        if valor > max:
            maxI = i
            max = valor
    return maxI

lista = [1,2,3,4]

print(max_idx(lista))