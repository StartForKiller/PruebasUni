a_term = float(input("Cuál es el coeficiente de x**2:"))
b_term = float(input("Cuál es el coeficiente de x:"))
c_term = float(input("Cuál es el coeficiente independiente:"))

sqrt_term = (b_term**2 - 4 * a_term * c_term)**0.5

solucion1 = (-b_term + sqrt_term) / (2 * a_term)
solucion2 = (-b_term - sqrt_term) / (2 * a_term)
print("Las soluciones son x1: {}, x2: {}".format(solucion1, solucion2))