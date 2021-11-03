n = int(input("Deme un número n: "))
a = int(input("Deme un número a: "))

x = 0
menor = n + 1
while x <= n:
    nx = n - x
    zero_x = 0
    count = 0
    while nx <= n:
        count += nx - zero_x
        nx += 1

    if count == a:
        if x < menor:
            menor = x

    x += 1

if menor != (n + 1):
    print("El menor entro x es: {}".format(menor))
else:
    print("No existe menor")