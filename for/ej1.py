n = int(input("Dame un número: "))

suma = 0
for i in range(n, 0, -1):
    suma += i

print("La suma de los n primeros número naturales es {}".format(suma))