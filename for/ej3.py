n = int(input("Dame un número: "))

cadena = ''
for i in range(n, 0, -1):
    cadena += '*'

print("La cadena es {}".format(cadena))