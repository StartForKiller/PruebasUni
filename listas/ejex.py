def norma2(lista1, lista2):
    suma = 0
    for (el1, el2) in zip(lista1, lista2):
        el = el1-el2
        suma += el*el
    return (suma**0.5)/len(lista1)

lista1 = [1.1, 2.2, 3.3, 4.4]
lista2 = [1.5, 2.0, 3.7, 4.2]

print("La norma de {} - {} es: {}".format(lista1, lista2, norma2(lista1, lista2)))