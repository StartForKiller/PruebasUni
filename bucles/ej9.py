umbral = int(input("Introduzca el umbral: "))

print("Sucesión de Fibonnaci: 0", end='')

a = 0
b = 1
while b < umbral:
    print(", {}".format(b), end='')

    c = b
    b = a + b
    a = c

print()