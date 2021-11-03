nombre = input("¿Cuál es tu nombre?:")
nota1 = float(input("Primera nota:"))
nota2 = float(input("Segunda nota:"))

nota_media = (nota1 + nota2) / 2

print("La nota media de {} es {}".format(nombre, nota_media))
print("Aprueba la asignatura: {}".format(nota_media >= 5.0))