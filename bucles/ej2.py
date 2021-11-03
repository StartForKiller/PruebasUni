while num < 0:
    num = int(input("De un número: "))
    if num < 0:
        print("El número {} es negativo".format(num))

print("El número {} es positivo".format(num))