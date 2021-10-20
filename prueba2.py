tipo = input('selecciona el tipo de grados, c: celsius | f: farenheid: ')
grados = float(input('Selecciona los grados: '))
if tipo == 'c':
    gradosFarenheid = grados * 9 / 5 + 32
    print('Grados farenheid:', gradosFarenheid)
elif tipo == 'f':
    gradosCelsius = (grados - 32) * 5 / 9
    print('Grados celsius:', gradosCelsius)