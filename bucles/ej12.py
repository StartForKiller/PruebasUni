n = int(input("Introduzca un número: "))

prueba = n - 1
primo = True
while prueba > 1:
    if n % prueba == 0:
        primo = False
        break
    prueba -= 1

if n <= 1 or not primo:
    print("El número {} no es primo".format(n))
else:
    print("El número {} es primo".format(n))