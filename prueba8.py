n1 = int(input("Número 1:"))
n2 = int(input("Número 2:"))
n3 = int(input("Número 3:"))
n4 = int(input("Número 4:"))
n5 = int(input("Número 5:"))

def esMayor(n) -> bool:
    return n >= n1 and n >= n2 and n >= n3 and n >= n4 and n >= n5

if esMayor(n1):
    print("El mayor es {}".format(n1))
elif esMayor(n2):
    print("El mayor es {}".format(n2))
elif esMayor(n3):
    print("El mayor es {}".format(n3))
elif esMayor(n4):
    print("El mayor es {}".format(n4))
else:
    print("El mayor es {}".format(n5))
