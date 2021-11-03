
suma_par = suma_impar = count = num = 0
while num >= 0:
    num = int(input("De un número: "))
    if num >= 0:
        if count % 2 == 0:
            suma_par += num
        else:
            suma_impar += num
        count += 1

print("La media par es {}".format(suma_par / (count // 2 + count % 2)))
print("La media impar es {}".format(suma_impar / (count // 2)))