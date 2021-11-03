dividendo = float(input("Introduzca el dividendo: "))
divisor = float(input("Introduzca el dividendo: "))

suma = 0
count = 0
while (suma + divisor) < dividendo:
    count += 1
    suma += divisor

print("Cociente: {} // {} = {}".format(dividendo, divisor, count))
print("Resto: {} % {} = {}".format(dividendo, divisor, dividendo - suma))