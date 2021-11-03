tipo = input('selecciona el tipo de grados, c: celsius | f: farenheid: ')
grados = float(input('Selecciona los grados: '))
if tipo == 'c':
    gradosFarenheid = grados * 9 / 5 + 32
    print('Grados farenheid:', gradosFarenheid)
elif tipo == 'f':
    gradosCelsius = (grados - 32) * 5 / 9
    print('Grados celsius:', gradosCelsius)

V_i = 20
a = 9.8
t = 30
V_f = V_i + a*t
print(V_f)

base = 9
altura = 5
area = str(base * altura / 2)
mensaje = 'El area del triangulo es igual a ' + area
print(mensaje)

base = 5
altura = 7
area = base * altura / 2
mensaje = 'El area del triangulo es igual a ' + str(area)
print(mensaje)

anyo = 2011
bisiesto = (anyo % 4 == 0) and not(anyo % 100 == 0 and not(anyo % 400 == 0))
print(bisiesto)


kilos = 12
libras = kilos * 0.45359237
print(libras)


V_i = 20
a = 9.8
t = 30
D = V_i * t + (1 / 2) * a * t**2
print(D)

V_i = -((1/2) * a * t**2 - D)