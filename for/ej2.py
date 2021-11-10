n = int(input("Dame un número: "))

factorial = 1
for i in range(n, 0, -1):
    factorial *= i

print("El factorial n es {}".format(factorial))