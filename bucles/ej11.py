n = int(input("Introduzca un número: "))

cadena_bin = ''
while n != 0:
    cadena_bin += "{}".format(n % 2)
    n //= 2

print("El número en binario es: ", end='')

if cadena_bin == '':
    print('0')
else:
    print(cadena_bin[::-1])