mayor = posicion = count = 0
while True:
    count += 1
    num = int(input("Introduzca un número: "))
    if num == 0:
        break
    elif num > mayor:
        mayor = num
        posicion = count

print("El mayor número es {} y se proporcionó en la posición {}".format(mayor, posicion))