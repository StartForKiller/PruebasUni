n1 = int(input("Número 1:"))
n2 = int(input("Número 2:"))
n3 = int(input("Número 3:"))

if n1 <= n2 and n2 <= n3:
    print("Los número están ordenados de manera ascendente")
elif n1 >= n2 and n2 >= n3:
    print("Los número están ordenados de manera descendente")
else:
    print("Los número no están ordenados")