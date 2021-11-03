import sys

print('Meta el texto que le venga en gana, para salir poner ".":')

count = 0
while True:
    char = input()
    if char == 'a':
        count += 1
    elif char != '.':
        break

print('Has introducido {} letras a'.format(count))