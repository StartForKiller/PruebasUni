
suma = count = num = 0
while num >= 0:
    num = int(input("De un número: "))
    if num >= 0:
        suma += num
        count += 1

if count != 0:
    print("La media es {}".format(suma / count))
else:
    print("No se puede calcular la media")