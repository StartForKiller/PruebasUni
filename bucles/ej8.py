num = int(input("De un número: "))

print("Las cifras del número {} de la menos a la más significativa son: ".format(num), end='')
cifras = ''
while num != 0:
    cifras += "{}".format(num % 10)
    num //= 10

print('{}'.format(0 if cifras == '' else cifras))