numero = float(input("Dame un número:"))
opcion = input("ESCOGE UNA OPCIÓN. Calcular:\n\ta) El cuadrado del número\n\tb) El cubo del número\n\tc) El doble del número\nOpción?")

if opcion == "a":
    print("El cuadrado de {} es {}".format(numero, numero**2))
elif opcion == "b":
    print("El cubo de {} es {}".format(numero, numero**3))
elif opcion == "c":
    print("El doble de {} es {}".format(numero, numero*2))
else:
    print("La opción {} no existe".format(opcion))