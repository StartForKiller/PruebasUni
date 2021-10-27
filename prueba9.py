a_term = float(input("Dame el coeficiente de las x:"))
b_term = float(input("Dame el coeficiente independiente:"))

if a_term == 0 and b_term == 0:
    print("La ecuación tiene infinitas soluciones")
elif a_term == 0:
    print("La ecuación no tiene solución")
else:
    print("La solucíon es {}".format(-b_term/a_term))
