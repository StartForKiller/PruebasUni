anno = int(input("Introduzca un año:"))
mes = int(input("Introduzca un mes:"))

bisiesto = (anno % 4 == 0) and not(anno % 100 == 0 and anno % 400 != 0)

if bisiesto:
    print("El año {} es bisiesto".format(anno))
else:
    print("El año {} no es bisiesto".format(anno))

if mes == 2: # Febrero
    print("El mes {} tiene {} días".format(mes, 29 if bisiesto else 28))
else:
    print("El mes {} tiene {} días".format(mes, 31 if mes % 2 == 1 else 30))