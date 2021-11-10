suma = 0
for i in range(1, 101):
    suma += (i^2 + 1) / i

print("Resultado: {}".format(suma))