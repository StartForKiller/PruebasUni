import math

a_term = float(input("Cuál es el coeficiente de x**2:"))
b_term = float(input("Cuál es el coeficiente de x:"))
c_term = float(input("Cuál es el coeficiente independiente:"))

sqrt_term = b_term**2 - 4 * a_term * c_term

if sqrt_term >= 0:
    solucion1 = (-b_term + math.sqrt(sqrt_term)) / (2 * a_term)
    solucion2 = (-b_term - math.sqrt(sqrt_term)) / (2 * a_term)
    print("Las soluciones son x1: {}, x2: {}".format(solucion1, solucion2))
else:
    print("No hay soluciones reales")