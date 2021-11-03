nota1 = int(input("Primera nota:"))
nota2 = int(input("Segunda nota:"))
nota3 = int(input("Tercera nota:"))
nota4 = int(input("Cuarta nota:"))

media = (nota1 + nota2 + nota3 + nota4) / 4

print("La nota media es {}, Grado ".format(media), end="")
if media >= 90:
    print("A")
elif media >= 80:
    print("B")
elif media >= 70:
    print("C")
elif media >= 60:
    print("D")
else:
    print("E")